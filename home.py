#1 hardcoded response

import streamlit as st
import numpy as np

from secret import getResponse


st.title('Welcome to IVR Resolution Bot')
st.write('Welcome to the home page')

with st.chat_message("assistant"):
    st.write("Welcome to IVR Resolution Bot")


inpu = "How can I help you?"
   
prompt = st.chat_input(inpu)

if prompt:
    resolution = getResponse(prompt)
    st.write(f"You asked: {prompt}")
    st.write(f"Resolution: {resolution}")
