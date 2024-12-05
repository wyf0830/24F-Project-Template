import streamlit as st
import requests

# Update API_URL based on your deployment
# If running locally without Docker, use 'http://localhost:4000/a/employers'
# If using Docker and 'api' resolves correctly, keep as 'http://api:4000/a/employers'
API_URL = 'http://api:4000/a/employers'

st.title("Update Employer Information")

# View Employers
st.subheader("Employer List")

try:
    response = requests.get(API_URL)
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
    employers = response.json()
    st.dataframe(employers)
except requests.exceptions.RequestException as e:
    st.error(f"Error fetching employers: {e}")

# Add Employer
st.subheader("Add Employer")
name = st.text_input("Name")
contact_info = st.text_input("Contact Info")
industry = st.text_input("Industry")
profile_status = st.selectbox("Profile Status", options=[1, 0], format_func=lambda x: 'Active' if x == 1 else 'Inactive')

if st.button("Add Employer"):
    if not name or not contact_info:
        st.error("Please provide both Name and Contact Info.")
    else:
        payload = {
            "name": name,
            "contact_info": contact_info,
            "industry": industry,
            "profile_status": profile_status
        }
        try:
            post_response = requests.post(API_URL, json=payload)
            if post_response.status_code == 201:
                st.success("Employer added successfully!")
            else:
                # Attempt to extract error message from response
                try:
                    error_info = post_response.json()
                    error_message = error_info.get('error', 'Unknown error.')
                except ValueError:
                    error_message = post_response.text
                st.error(f"Failed to add employer. Status Code: {post_response.status_code}\nResponse: {error_message}")
        except Exception as e:
            st.error(f"Error: {e}")