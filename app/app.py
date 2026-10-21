
import streamlit as st
import tempfile
from model_helper import predict

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload the file", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded File", width="stretch")

    # Save the uploaded image to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
        temp_file.write(uploaded_file.getvalue())
        image_path = temp_file.name

    prediction = predict(image_path)
    st.info(f"Predicted Class: {prediction}")