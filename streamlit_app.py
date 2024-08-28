import streamlit as st

st.title("ENCRYPTION TEACHING TOOL?")
st.write("Select the encryption method that you would like to discover more about")


st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
