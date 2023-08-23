import streamlit as st
from rembg import remove
from PIL import Image 

def main():
    st.title("Alpha Matting")
    uploaded_file = st.file_uploader("Upload an image",type=["png","jpg","jpeg"],accept_multiple_files=False)
    if st.button("Generate"):
        if uploaded_file:
            img = Image.open(uploaded_file)
            res = bg_remove(img)
            col1, col2 = st.columns(2,gap='medium')
            with col1:
                st.write("## Original Image")
                st.image(img)
            with col2:
                st.write("## Result Image")
                st.image(res)
            
        else: 
            st.warning("Please upload an image")


def bg_remove(image):
    return remove(image)


if __name__ == "__main__":
    main()