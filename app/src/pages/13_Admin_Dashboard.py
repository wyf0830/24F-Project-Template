import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks

SideBarLinks()

# API endpoint for admin data
API_URL = "http://api:4000/a/admin_data"

# Page title
st.title("Admin Data Dashboard")

# View Admin Data
st.subheader("Admin Data List")

# Define the desired column order
desired_order = [
    "Log_ID", "Event_Type", "Log_Message", "Log_Time_Stamp", 
    "Report_ID", "Report_Content", "Report_Date", 
    "Report_Type", "Schedule_ID", "Backup_Frequency", 
    "Last_Backup_Date"
]

try:
    response = requests.get(API_URL)
    response.raise_for_status() 

    # Convert JSON response to a Pandas DataFrame
    dashboard = response.json()
    admin_dashboard = pd.DataFrame(dashboard)

    # Check if all desired columns exist
    missing_columns = [col for col in desired_order if col not in admin_dashboard.columns]
    if missing_columns:
        st.error(f"The following columns are missing from the data: {missing_columns}")
    else:
        # Reorder the columns
        admin_dashboard = admin_dashboard[desired_order]

        # Display the reordered DataFrame in Streamlit
        st.dataframe(admin_dashboard)

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching data: {e}")

st.write("---")
st.subheader("Add New Admin Data")

# Form for adding new data
with st.form("add_admin_data"):
    # Optional Admin_ID field
    admin_id = st.number_input("Admin ID", min_value=1, step=1, help="Provide the Admin ID if required")

    st.write("### Add System Log")
    event_type = st.text_input("Event Type", help="Type of event for the system log (e.g., System Update)")
    log_message = st.text_area("Log Message", help="Detailed description of the system event")

    st.write("---")
    st.write("### Add Report")
    report_content = st.text_area("Report Content", help="Content of the report")
    report_type = st.text_input("Report Type", help="Type of report (e.g., Performance, Backup)")

    st.write("---")
    st.write("### Add Backup Schedule")
    backup_frequency = st.text_input("Backup Frequency", help="Frequency of backups (e.g., Daily, Weekly)")

    # Submit button
    submit_button = st.form_submit_button(label="Add Data")

# Handle form submission
if submit_button:
    # Validate at least one field is provided
    if not (event_type or log_message or report_content or report_type or backup_frequency):
        st.error("At least one field must be filled to add data.")
    else:
        # Build the payload for the POST request
        payload = {
            "Admin_ID": int(admin_id) if admin_id else None,
            "Event_Type": event_type,
            "Log_Message": log_message,
            "Report_Content": report_content,
            "Report_Type": report_type,
            "Backup_Frequency": backup_frequency
        }

        try:
            # Send POST request to the API
            response = requests.post(API_URL, json=payload)
            if response.status_code == 201:
                st.success("Data added successfully!")
            else:
                # Handle server errors
                error_message = response.json().get("error", "Unknown error.")
                st.error(f"Failed to add data. Error: {error_message}")

        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to the server: {e}")