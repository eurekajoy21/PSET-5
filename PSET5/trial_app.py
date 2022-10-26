import streamlit as st
from PIL import Image


button = st.button("Click me!")
if button:
    st.header("BOO!")
    image = Image.open('images/cat.png')
    st.image(image)
    
