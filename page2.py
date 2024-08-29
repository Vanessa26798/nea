import streamlit as st

st.page_link("https://encryption-teaching-tool.streamlit.app/", label="Home page")

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
