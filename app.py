import os
import streamlit as st
from PIL import Image
from caption_generator import generate_caption

st.set_page_config(page_title="AI Image Captioning", layout="centered")
st.title("🖼️ AI-Powered Image Captioning")
st.markdown("Upload one or more images, and get AI-generated captions instantly.")

# Upload images
uploaded_files = st.file_uploader(
    "Choose image files (JPG, JPEG, PNG)", 
    type=["jpg", "jpeg", "png"], 
    accept_multiple_files=True
)

captions_output = []

if uploaded_files:
    st.markdown("### Results")
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        with st.spinner("Generating caption..."):
            caption = generate_caption(image)

        st.success("**Caption:** " + caption)
        captions_output.append(f"{uploaded_file.name}: {caption}")
        st.markdown("---")

    # Download captions
    if captions_output:
        captions_text = "\n".join(captions_output)
        st.download_button("📄 Download Captions as .txt", captions_text, file_name="captions.txt")
else:
    st.info("Please upload at least one image to generate captions.")
