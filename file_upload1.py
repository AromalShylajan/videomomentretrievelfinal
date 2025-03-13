
import streamlit as st

uploaded_file = st.file_uploader("Choose a video file", type="mp4")

if uploaded_file is not None:
    with open("video/video.mp4", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File saved successfully!")
