import streamlit as st
import pandas as pd
import numpy as np

# Title of the app str
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


# Displaying Colored Text/Bootstreap Alert
st.success("Successful")
st.warning("This is Danger")
st.info("This is information")
st.error("This is an error")
st.exception("This is an exception")

# Superfunction
st.write("Normal Text")
st.write("## This is a markdown text")
st.write(1+2)
st.write(dir(st))

# Help Info
st.help(range)





