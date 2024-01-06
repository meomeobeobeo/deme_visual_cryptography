import os
import sys
sys.path.insert(0, './src')

import streamlit as st

from PIL import Image
from src.lsb_stegno import lsb_encode, lsb_decode
from src.n_share import generate_shares, compress_shares
import chardet

menu = st.sidebar.radio('Options', ['Docs', 'Encode', 'Decode'])


if menu == 'Docs':
    st.title('Documentation')

    # Detect the encoding of the file
    with open('README.md', 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']

    # Read the file using the detected encoding
    with open('README.md', 'r', encoding=encoding) as f:
        docs = f.read()

    st.markdown(docs, unsafe_allow_html=True)

elif menu == 'Encode':
    st.title('Encoding')

    # Image
    img = st.file_uploader('Upload image file', type=['jpg', 'png', 'jpeg'])
    if img is not None:
        img = Image.open(img)
        try:
            img.save('images/img.jpg')
        except:
            img.save('images/img.png')
        st.image(img, caption='Selected image to use for data encoding',
                use_column_width=True)

    # Data
    txt = st.text_input('Message to hide')

    # Encode message
    if st.button('Encode data and Generate shares'):

        # Checks
        if len(txt) == 0:
            st.warning('No data to hide')
        elif img is None:
            st.warning('No image file selected')

        # Generate splits
        else:
            generate_shares(lsb_encode(txt))
            try:
                os.remove('images/img.jpg')
            except FileNotFoundError:
                os.remove('images/img.png')
            st.success('Data encoded, Shares generated in folder [images]')
            image1 = Image.open("images/pic1.png")
            image2 = Image.open("images/pic2.png")
            # Display the images using Streamlit
            st.image([image1, image2], caption=['Share1 image', 'Share2 image'], use_column_width=True)
            

        

elif menu == 'Decode':
    st.title('Decoding')

    # Share 1
    img1 = st.file_uploader('Upload Share 1', type=['png'])
    if img1 is not None:
        img1 = Image.open(img1)
        img1.save('images/share1.png')
        st.image(img1, caption='Share 1', use_column_width=True)

    # Share 2
    img2 = st.file_uploader('Upload Share 2', type=['png'])
    if img2 is not None:
        img2 = Image.open(img2)
        img2.save('images/share2.png')
        st.image(img2, caption='Share 2', use_column_width=True)

    # Decode message
    if st.button('Hợp nhất 2 shares and giải mã thông điệp'):

        # Check
        if img1 is None or img2 is None:
            st.warning('Upload both shares')

        # Compress shares
        else:
            compress_shares()
            os.remove('images/share1.png')
            os.remove('images/share2.png')
            st.success('Decoded message: ' + lsb_decode('images/compress.png'))
            
            imageCompress = Image.open("images/compress.png")
             # Display the images using Streamlit
            st.image([imageCompress], caption=['Ảnh hợp nhất'], use_column_width=True)
