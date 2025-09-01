import streamlit as st
import requests
 
st.title("Multimodal Assistant")
option = st.radio("Choose query type:", ["Text", "Image"])
 
if option == "Text":
    user_input = st.text_area("Enter your question:")
    if st.button("Ask"):
      with st.spinner("Loading..."):
        response = requests.post("http://localhost:8000/ask/text", data={"query": user_input})
        try:
            result = response.json()
            st.write("Response:", result["response"])
        except Exception as e:
            st.error("Failed to get a valid response from backend.")
            st.text(f"Raw response: {response.text}")
            st.text(f"Error: {e}")
 
elif option == "Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])
    if uploaded_file and st.button("Analyze"):
     with st.spinner("Loading..."):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8000/ask/image", files=files)
        try:
            result = response.json()
            st.write("Response:", result["response"])
        except Exception as e:
            st.error("Failed to get a valid response from backend.")
            st.text(f"Raw response: {response.text}")
            st.text(f"Error: {e}")
 