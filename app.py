import streamlit as st
import os


# Print the current working directory
print("Current working directory:", os.getcwd())

# Set Streamlit page config
st.set_page_config(page_title="Restaurant Management System", layout="wide")

# Page Navigation
page = st.sidebar.radio("Navigate", ["Home", "Login", "Register", "Restaurant Management"])


if page == "Home":
    st.write("You are on the Home Page.")
elif page == "Login":
    st.write("You are on the Login Page.")
elif page == "Register":
    st.write("You are on the Register Page.")
elif page == "Restaurant Management":
    st.write("You are on the Restaurant Management Page.")
