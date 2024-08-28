import streamlit as st

st.title("ENCRYPTION TEACHING TOOL")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)


