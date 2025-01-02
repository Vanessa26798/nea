import streamlit as st
import random


st.title("ENCRYPTION TEACHING TOOL")
st.write("Select the encryption method that you would like to discover more about")

import time
import numpy as np
import pandas as pd
import streamlit as st

_LOREM_IPSUM = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""


def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)


if st.button("Stream data"):
    st.write_stream(stream_data)



col1, col2 = st.columns(2)

with col1:
    st.header("Caesar cipher")
    st.info('A substitution cipher where each letter of the plaintext is shifted ahead by a fixed number of letters (key).')
    st.page_link("pages/Caesar.py", label="Click me")

with col2:
    st.header("Vernam cipher")
    st.info('An encryption that uses one-time pad which contributes to its perfect security.')
    st.page_link("pages/Vernam.py", label="Click me")

