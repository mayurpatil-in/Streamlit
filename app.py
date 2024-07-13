import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Hi Streamlit")

#Text
st.text("Hello World")

name = "Mayur"
st.text("This is {}".format(name))

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Title
st.title("This is a title")

#  Markdown
st.markdown("This is markdown")
st.markdown("# This is markdown")
st.markdown("## This is markdown")