import streamlit as st

# Set up the page
st.set_page_config(page_title="Contact Us", page_icon="📞")

# Title
st.title("Contact Us")

# Informational Text
st.write("""
We’d love to hear from you! Whether you have a question, feedback, or a concern, you can reach out to us using the form below.
""")

# Create a contact form using Streamlit's form functionality
with st.form(key='contact_form'):
    # Form fields
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    subject = st.selectbox("Subject", ["General Inquiry", "Support", "Partnership", "Other"])
    message = st.text_area("Message")

    # Submit button
    submit_button = st.form_submit_button(label='Submit')

# Handle form submission
if submit_button:
    if name and email and message:
        st.success(f"Thank you, {name}! We have received your message and will get back to you soon.")
        # Here you could also process the data, e.g., sending an email or saving it to a database
    else:
        st.error("Please fill in all the fields before submitting.")
