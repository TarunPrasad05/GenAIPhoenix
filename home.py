#1 hardcoded response

import streamlit as st
import numpy as np

from secret import getResponse


st.title('Home')
st.write('Welcome to the home page')
st.write('This is a hardcoded response')

with st.chat_message("assistant"):
    st.write("Hello 123")
    st.bar_chart(np.random.randn(50, 3))

    
prompt = st.chat_input("How can I help you?")
if prompt:
    resolution = getResponse(prompt)
    st.write(f"You asked: {resolution}")
