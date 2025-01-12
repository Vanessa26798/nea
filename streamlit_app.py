import streamlit as st
import random


st.title("ENCRYPTION TEACHING TOOL")
st.write("Select the encryption method that you would like to discover more about")

col1, col2 = st.columns(2)

with col1:
    st.header("Caesar cipher")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Caesar_cipher_left_shift_of_3.svg/1920px-Caesar_cipher_left_shift_of_3.svg.png")
    st.info('A substitution cipher where each letter of the plaintext is shifted ahead by a fixed number of letters (key).')
    st.page_link("pages/Caesar.py", label="Click me")

with col2:
    st.header("Vernam cipher")
    st.image("https://www.cryptomuseum.com/crypto/svg/xor3.svg")
    st.info('An encryption that uses one-time pad which contributes to its perfect security.')
    st.page_link("pages/Vernam.py", label="Click me")

