import streamlit as st
from PIL import Image
from model_pipeline import predict_image
from visual_elements import apply_custom_css


st.set_page_config(
    page_title = "Car Damage Detector",
    layout = "wide"
)

apply_custom_css()  # Apply the custom CSS styles

#-- Sidebar --
with st.sidebar:
    st.header("How it works")
        
    st.markdown("""
        1. **Upload image** - drag & drop or browse for an image of car damage
        2. **Analyze** - wait while the CNN processes it
        3. **View Results** - inspect the location and condition details.
        """)
        
        
    #Model details card
    st.markdown("""
        <div class="sidebar-card">
            <span style="color: #A0AEC0;">Model:</span> ConvNeXT<br>
            <span style="color: #A0AEC0;">Avg Precision:</span> 83.13%
        </div>
        """, unsafe_allow_html=True)
    


#-- Main area --
spacer_left, main_col, spacer_right = st.columns([1, 5, 1])
with main_col:
    st.title("🚙 Car Damage Detector")

    # File uploader
    uploaded_file = st.file_uploader(
        "Drag and drop file here / Limit 200MB per file - JPG, PNG, JPEG", 
        type=["jpg", "png", "jpeg"]
    )

    output = ["--", "--"] # Fixed potential index error when no file is uploaded
    confidence_score = 0.0
    
    if uploaded_file:
        image_path = "temp_image.jpg"

        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Constrain image size further and center it to prevent massive scaling
        img_spacer1, img_col, img_spacer2 = st.columns([1, 2.5, 1])
        with img_col:
            with st.container(width = 600, height = 250):
                st.image(image_path, use_container_width=True)

        with st.spinner("Analyzing the image..."):
            predicted_class, confidence_score = predict_image(image_path)

        output = predicted_class.split(" ")

    # Result columns
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label = "Predicted Class (View)", value = output[0])

    with col2:
        st.metric(label = "Damage Condition", value = output[1])


    # Confidence bar
    st.write("\n")
    col_text_1, col_text_2 = st.columns([9, 1])

    with col_text_1:
        st.markdown("Analysis Confidence")

    with col_text_2:
        st.markdown(f"**{int(confidence_score * 100)}%**")

    st.progress(int(confidence_score * 100))
