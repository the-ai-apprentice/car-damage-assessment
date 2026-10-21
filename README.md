# 🚙 Vehicle Damage Detector

![Streamlit](https://img.shields.io/badge/Streamlit-1.64.0-FF4B4B?style=flat&logo=streamlit)
![PyTorch](https://img.shields.io/badge/PyTorch-2.14.1-EE4C2C?style=flat&logo=pytorch)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python)

A sleek, dark-themed web application that uses Deep Learning to analyze vehicle images and detect damage. Built with **Streamlit** and a fine-tuned **PyTorch ConvNeXT Tiny** model, this tool classifies both the vehicle's view (Front/Rear) and its condition (Normal, Breakage, Crushed) in seconds.

## ✨ Features
* 🖼️ **Drag & Drop Upload:** Easily upload vehicle images (JPG, PNG, JPEG).
* 🧠 **Deep Learning Powered:** Uses a customized `ConvNeXT` architecture for high-accuracy image classification.
* ⚡ **Fast Inference:** Model weights are cached in memory for rapid predictions.
* 🎨 **Custom Dark UI:** Fully customized CSS styling with glowing metric cards and edge-to-edge dark mode design.

## 📂 Project Structure

```text
📦 Vehicle-Damage-Detector
 ┣ 📂 artifacts
 ┃ ┗ 📜 saved_model.pth          # Fine-tuned PyTorch model weights (ConvNeXT)
 ┣ 📜 main_3.py                  # Main Streamlit application frontend
 ┣ 📜 model_pipeline.py          # PyTorch model architecture and inference logic
 ┣ 📜 visual_elements_2.py       # Custom CSS injection for the UI styling`
 ┗ 📜 requirement.txt            # Python dependencies (Streamlit, Torch, Pillow)
```

## 🚀 Getting Started

**1. Clone the repository**
```bash
git clone [https://github.com/yourusername/vehicle-damage-segmentation.git]
cd vehicle-damage-segmentation
```

**2. Install dependencies**
Make sure you have Python installed, then run the following command to install the required libraries:
```bash
pip install -r requirement.txt
```

**3. Add the model weights**
Ensure your trained model weights file (`saved_model.pth`) is placed inside the `artifacts/` directory.

**4. Run the application**
Launch the Streamlit server:
```bash
streamlit run main.py
```
The app will open automatically in your browser at `http://localhost:8501`.

## 🛠️ Built With
* **Streamlit:** For the interactive web interface.
* **PyTorch & TorchVision:** For model architecture and tensor transformations.
* **ConvNeXT:** The backbone convolutional neural network used for feature extraction.
* **Pillow (PIL):** For handling image uploads.

## 📝 Classes Detected
The model is trained to recognize the following 6 categories:
1. Front Normal
2. Front Breakage
3. Front Crushed
4. Rear Normal
5. Rear Breakage
6. Rear Crushed
