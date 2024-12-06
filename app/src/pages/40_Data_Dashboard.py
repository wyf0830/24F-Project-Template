import streamlit as st
import requests

# Update API_URL based on your deployment
# If running locally without Docker, use 'http://localhost:4000/a/employers'
# If using Docker and 'api' resolves correctly, keep as 'http://api:4000/a/employers'
#API_URL = 'http://api:4000/d/data_dashboard'
API_URL = 'http://api:4000/d/data_dashboard'

st.title("Program Director Data Dashboard")

# View Employers
st.subheader("Director Data List")

try:
    response = requests.get(API_URL)
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
    employers = response.json()
    st.dataframe(employers)
except requests.exceptions.RequestException as e:
    st.error(f"Error fetching employers: {e}")