import streamlit as st
import requests

# Update API_URL based on your deployment
API_URL = 'http://api:4000/a/employers'

st.title("Remove Employer")

# View Employers
st.subheader("Employer List")

try:
    response = requests.get(API_URL)
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
    employers = response.json()
    if employers:
        # Allow the user to select an employer to delete
        employer_to_delete = st.selectbox(
            "Select an Employer to Delete",
            employers,
            format_func=lambda x: f"{x['Employer_ID']} - {x['Name']}"
        )
    else:
        st.info("No employers found.")
        employer_to_delete = None
except requests.exceptions.RequestException as e:
    st.error(f"Error fetching employers: {e}")
    employer_to_delete = None

# Delete Employer
if employer_to_delete and st.button("Delete Employer"):
    try:
        delete_url = f"{API_URL}/{employer_to_delete['Employer_ID']}"
        delete_response = requests.delete(delete_url)
        if delete_response.status_code == 200:
            st.success(f"Employer {employer_to_delete['Name']} deleted successfully!")
        else:
            error_message = delete_response.json().get('error', 'Unknown error.')
            st.error(f"Failed to delete employer: {error_message}")
    except Exception as e:
        st.error(f"Error deleting employer: {e}")
