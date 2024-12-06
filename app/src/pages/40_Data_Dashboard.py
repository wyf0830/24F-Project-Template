import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Update API_URL based on your deployment
# If running locally without Docker, use 'http://localhost:4000/a/employers'
# If using Docker and 'api' resolves correctly, keep as 'http://api:4000/a/employers'
API_URL = 'http://api:4000/d/dashboard'

st.title("Program Director Data Dashboard")

# View Employers
st.subheader("Director Data List")

try:
    response = requests.get(API_URL)
    response.raise_for_status() 

    # Convert JSON response to a Pandas DataFrame
    dashboard = response.json()
    director_dashboard = pd.DataFrame(dashboard)

    # Define desired column order
    desired_order = [
        'Director_ID', 'Director_Name', 'Director_Contact', 
        'Resource_Allocation_ID', 'Resource_Type', 'Performance_Report_Date', 
        'Performance_Summary', 'Metrics_Name', 'Student_ID', 
        'Student_Name', 'Student_Major', 'Student_Program', 'Employer_Feedback'
    ]

    # Check if all desired columns are present
    missing_columns = [col for col in desired_order if col not in director_dashboard.columns]
    if missing_columns:
        st.error(f"Missing columns in the data: {missing_columns}")
    else:
        # Reorder the columns
        director_dashboard = director_dashboard[desired_order]

    # Display the reordered DataFrame in Streamlit
    st.dataframe(director_dashboard)

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching data: {e}")

# Add Employer
st.subheader("Add Information")
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