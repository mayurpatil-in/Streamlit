import streamlit as st

# Working with Widgets
# Buttons/Radio/Checkbox/Select

# Working with Buttons
name = "Mayur"
if st.button("Submit"):
   st.write("Name: {}".format(name.upper()))

if st.button("Submit",key='new02'):
   st.write("First Name: {}".format(name.lower()))

# Working with RadioButtons
status = st.radio("What is your status",("Active","Inactive"))
if status == 'Active':
   st.success("You are active")
elif status == 'Inactive':
   st.warning("Inactive")

# Working with Checkbox
if st.checkbox("Show/Hide"):
   st.text("Showing something")

# Working with Beta Expander
st.title("Streamlit Expander Example")

with st.expander("Python"):
    st.success("Hello Python")