import streamlit as st
import pandas as pd
import hashlib
import os

USER_DB_PATH = 'user_data.csv'

# Check if the CSV file exists, if not, create it
if not os.path.exists(USER_DB_PATH):
    columns = ['Username', 'Password', 'Email', 'Contact Number', 'Address']
    pd.DataFrame(columns=columns).to_csv(USER_DB_PATH, index=False)

# Function to hash the password before storing it
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to add new user to CSV
def add_user(username, password, email, contact_number, address):
    # Read the current users from the CSV file
    users = pd.read_csv(USER_DB_PATH)
    
    # Hash the password before saving
    hashed_password = hash_password(password)
    
    # Create a new user DataFrame
    new_user = pd.DataFrame({
        'Username': [username], 
        'Password': [hashed_password], 
        'Email': [email], 
        'Contact Number': [contact_number], 
        'Address': [address]
    })
    
    # Append the new user to the existing users DataFrame
    users = pd.concat([users, new_user], ignore_index=True)
    
    # Write the updated DataFrame back to the CSV file
    users.to_csv(USER_DB_PATH, index=False)

# Registration page function
def register():
    st.title("Register Page")
    
    # Input fields for user registration
    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type='password')
    email = st.text_input("Email Address")
    contact_number = st.text_input("Contact Number")
    address = st.text_area("Address")
    
    # Debugging: Check what the inputs are
    st.write(f"Username: {username}")
    st.write(f"Password: {password}")
    st.write(f"Email: {email}")
    st.write(f"Contact Number: {contact_number}")
    st.write(f"Address: {address}")
    
    # Register button to trigger the registration process
    if st.button("Register"):
        # Check if all fields are filled
        if username and password and email and contact_number and address:
            add_user(username, password, email, contact_number, address)
            st.success("User registered successfully! Please login.")
        else:
            st.error("Please fill in all fields")

# Run the register function
register()
