import streamlit as st
import pandas as pd
import hashlib


USER_DB_PATH = 'user_data.csv'

# Hash the password for security
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def validate_user(username, password):
    users = pd.read_csv(USER_DB_PATH)
    hashed_password = hash_password(password)
    user = users[users['Username'] == username]
    
    if not user.empty and user['Password'].values[0] == hashed_password:
        return True
    return False

def login():
    st.title("Login Page")
    
    # User input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        if validate_user(username, password):
            st.success("Login successful!")
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.error("Invalid username or password")

login()
