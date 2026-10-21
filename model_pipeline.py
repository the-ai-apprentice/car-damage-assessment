import torch
from torch import nn
from torchvision import models, transforms
from PIL import Image

#configuring PyTorch
torch.set_num_threads(2) 

#global variable to hold the model in memory
trained_model = None

#class names
class_names = ['Front Breakage', 'Front Crushed', 'Front Normal', 'Rear Breakage', 'Rear Crushed', 'Rear Normal']


#redifine the exact architecture
class CarClassifierConvNeXt(nn.Module):
    def __init__(self, num_classes, drop_out = 0.5):
        super().__init__()

        #load the pre-trained model ConvNext
        self.model = models.convnext_tiny(weights = "DEFAULT")

        #freeze the base layers
        for param in self.model.parameters():
            param.requires_grad = False

        #unfreeze the final stage
        for param in self.model.features[7].parameters():
            param.requires_grad = True

        #replace the classification head
        self.model.classifier[2] = nn.Sequential(
            nn.Dropout(drop_out),
            nn.Linear(self.model.classifier[2].in_features, num_classes)
        )

    def forward(self, x):
        return self.model(x)

#prediction pipeline
#prediction pipeline
def predict_image(image_path):
    #load and convert image to RGB
    image = Image.open(image_path).convert("RGB")

    #apply the exact same transformations as during training
    image_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean = [0.485, 0.456, 0.406], std = [0.229, 0.224, 0.225])
    ])

    #add a batch dimension
    image_tensor = image_transforms(image).unsqueeze(0)

    global trained_model

    # Only load the model if it hasn't been loaded yet
    if not trained_model:
        trained_model = CarClassifierConvNeXt(num_classes = len(class_names))
        trained_model.load_state_dict(torch.load("artifacts/saved_model.pth"))
        trained_model = trained_model.to(memory_format = torch.channels_last)
        
    # Ensure tensor matches model memory format
    image_tensor = image_tensor.to(memory_format = torch.channels_last)

    # Prediction logic happens EVERY time, outside the 'if' block
    trained_model.eval()
    with torch.no_grad():
        output = trained_model(image_tensor)
        _, predicted_class = torch.max(output, 1)
        confidence_score = torch.softmax(output, dim = 1)[0][predicted_class].item()
        class_name = class_names[predicted_class.item()]

    return class_name, confidence_score
