import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks

SideBarLinks()

# Define API URL for Program Impact Reports
API_URL = 'http://api:4000/d/reports'

st.title("Program Performance Reports")

# Section: View Existing Performance Reports
st.subheader("Performance Reports Data")

try:
    response = requests.get(API_URL)
    response.raise_for_status() 

    # Convert JSON response to a Pandas DataFrame
    performance_data = response.json()
    performance_df = pd.DataFrame(performance_data)

    # Define desired column order
    desired_order = ['Director_ID', 'Director_Name', 'Director_Contact', 
                     'Report_ID', 'Performance_Summary', 
                     'Performance_Report_Date']

    # Check if all desired columns are present
    missing_columns = [col for col in desired_order if col not in performance_df.columns]
    if missing_columns:
        st.error(f"Missing columns in the data: {missing_columns}")
    else:
        # Reorder the columns
        performance_df = performance_df[desired_order]

        # Display the reordered DataFrame in Streamlit
        st.dataframe(performance_df)

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching data: {e}")

# Section: Generate a New Impact Report
st.write('')
st.write('')
st.subheader("Generate a New Performance Report")

# Input fields for creating a new report
director_id = st.number_input("Director ID", min_value=1, step=1, help="Enter the ID of the director.")
summary = st.text_area("Performance Summary", help="Provide a summary of the performance report.")
date = st.date_input("Report Date")

if st.button("Generate Report"):
    if not director_id or not summary or not date:
        st.error("Please provide all required fields!")
    else:
        # Prepare the payload for the POST request
        payload = {
            "Director_ID": director_id,  # Include Director_ID
            "Summary": summary,
            "Date": date.strftime('%Y-%m-%d')  # Convert date to string format for API
        }

        try:
            # Send POST request to create the report
            response = requests.post(API_URL, json=payload)
            if response.status_code == 201:
                st.success("Performance report generated successfully!")
            else:
                error_message = response.json().get('error', 'Unknown error occurred.')
                st.error(f"Failed to generate report: {error_message}")
        except Exception as e:
            st.error(f"Error: {e}")
# Section: Delete an Existing Performance Report
st.write('')
st.write('')
st.subheader("Delete an Existing Performance Report")

# Input for deleting a report
report_id_to_delete = st.number_input("Report ID to Delete", min_value=1, step=1)

if st.button("Delete Report"):
    try:
        # Send DELETE request to remove the report
        response = requests.delete(f"{API_URL}/{report_id_to_delete}")
        if response.status_code == 200:
            st.success("Performance report deleted successfully!")
        elif response.status_code == 404:
            st.error("Report not found.")
        else:
            error_message = response.json().get('error', 'Unknown error occurred.')
            st.error(f"Failed to delete report: {error_message}")
    except Exception as e:
        st.error(f"Error: {e}")
