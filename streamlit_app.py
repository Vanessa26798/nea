import streamlit as st

st.title("ENCRYPTION TEACHING TOOL")
st.write("Select the encryption method that you would like to discover more about")


Input = st.text_input("Input your own key (1) or a random key (2)? ", "")
if Input == "1": 
  st.write("The current movie title is", title)
