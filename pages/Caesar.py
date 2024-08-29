import streamlit as st
import random


st.page_link("https://encryption-teaching-tool.streamlit.app/", label="Homepage")

st.header("Caesar Encryption")

tab1, tab2 = st.tabs(["Caesar Encryption", "Vernam Encryption"])

with tab1:
    st.header("Caesar Encryption")
    Input = st.text_input("Input your own key (1) or a random key (2)? ", " ")
    if Input == "1":
        Key = st.text_input("Please enter the key: ", "")
        st.write("The key is ", Key)
    elif Input == "2": 
        Key = random.randrange(1, 26)
        st.write("The key is ", Key)
    elif Input != 1 and Input != 2: 
        st.write("Invalid input.")

with tab2:
    st.header("Vernam Encryption")
    st.write("tesing")



tab1, tab2, tab3, tab4 = st.tabs(["History", "Encrypt a plaintext", "Decrypt a ciphertext", "Weakness"])

with tab1:
    st.header("History")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
with tab2:
    st.header("Encryt a plaintext")
    Input = st.text_input("Input your own key (1) or a random key (2)? ", " ")
    if Input == "1":
        Key = st.text_input("Please enter the key: ", "")
        st.write("The key is ", Key)
    elif Input == "2": 
        Key = random.randrange(1, 26)
        st.write("The key is ", Key)
    elif Input != 1 and Input != 2: 
        st.write("Invalid input.")
with tab3:
    st.header("Decrypt a ciphertext")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab4: 
    st.header("Weakness")


