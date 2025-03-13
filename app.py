import streamlit as st
import youtube_download
import main
from transformers import pipeline
from PIL import Image
import streamlit as st


@st.cache_resource
def load_pipe():
    captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    return captioner


st.title('VIDEO MOMENT RETRIEVAL')
st.write('You can upload a video and use a query/a reference image to find the top three related moments in the video')

col1,col2 = st.columns(2,border=True)
uploaded_file = col1.file_uploader("Choose a video file", type="mp4")

if uploaded_file is not None:
    with open("video/video.mp4", "wb") as f:
        f.write(uploaded_file.getbuffer())
    col1.success("File saved successfully!")

# url = st.text_input('Enter youtube url')
img = col2.file_uploader('upload an image',type=['jpg','jpeg','png'])
if img:
    captioner = load_pipe()
    cap = captioner(Image.open(img))
    print(cap[0]['generated_text'])
    query = cap[0]['generated_text']
    col2.text(query)
else:
    query = col2.text_input('Enter your query')

if st.button('Find'):
    if uploaded_file:
        # youtube_download.download(url)
        frames = main.find(query)
        st.image(frames)

