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

# Update Director Data
st.subheader("Update Director Information")
director_id = st.number_input("Director ID", min_value=1, step=1)
updated_name = st.text_input("Updated Name")
updated_contact_info = st.text_input("Updated Contact Info")
updated_resource_type = st.text_input("Updated Resource Type")
updated_performance_date = st.date_input("Updated Performance Report Date")
updated_performance_summary = st.text_area("Updated Performance Summary")
updated_metrics_name = st.text_input("Updated Metrics Name")

if st.button("Update Director"):
    if not updated_name or not updated_contact_info:
        st.error("Please provide both Updated Name and Updated Contact Info.")
    else:
        # Build the payload for the PUT request
        update_payload = {
            "Director_Name": updated_name,
            "Director_Contact": updated_contact_info,
            "Resource_Type": updated_resource_type,
            "Performance_Report_Date": updated_performance_date.isoformat() if updated_performance_date else None,
            "Performance_Summary": updated_performance_summary,
            "Metrics_Name": updated_metrics_name
        }

        try:
            # Send PUT request to update director data
            update_response = requests.put(f"{API_URL}/{director_id}", json=update_payload)

            if update_response.status_code == 200:
                st.success("Director updated successfully!")
            elif update_response.status_code == 404:
                st.error("Director not found.")
            else:
                # Attempt to extract error message from response
                try:
                    error_info = update_response.json()
                    error_message = error_info.get('error', 'Unknown error.')
                except ValueError:
                    error_message = update_response.text
                st.error(f"Failed to update director. Status Code: {update_response.status_code}\nResponse: {error_message}")
        except Exception as e:
            st.error(f"Error: {e}")
