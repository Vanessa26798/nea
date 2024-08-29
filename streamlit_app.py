import streamlit as st
import random




st.title("ENCRYPTION TEACHING TOOL")
st.write("Select the encryption method that you would like to discover more about")
     


col1, col2 = st.columns(2)

with col1:
    st.header("Caesar cipher")
    st.info('Uses ...')
    st.page_link("pages/Caesar.py", label="Click me")

with col2:
    st.header("Vernam cipher")
    st.info('Uses ...')
    st.page_link("pages/Vernam.py", label="Click me")

