import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks


SideBarLinks()

# API URL for employers
API_URL = 'http://api:4000/a/employers'

st.title("Manage Employer Information")

# Fetch and Display Employers
st.subheader("Employer List")

try:
    # Getting data from the API
    response = requests.get(API_URL)
    response.raise_for_status()  # Raise an error for bad responses
    employer_data = response.json()

    # Convert JSON response to Pandas DataFrame
    employer_df = pd.DataFrame(employer_data)

    if not employer_df.empty:
        # Define the desired column order
        desired_order = ['Employer_ID', 'Name', 'Industry', 'Contact_Info', 'Profile_Status']
        employer_df = employer_df[desired_order]

        # Display the employer data in a table
        st.dataframe(employer_df)
    else:
        st.error("No employer data available.")

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching employer data: {e}")

# Update Employer
st.write("---")
st.subheader("Update Employer")

with st.form("update_employer_form"):
    employer_id_to_update = st.number_input("Enter Employer ID to Update", min_value=1, step=1)
    updated_name = st.text_input("Updated Name")
    updated_contact_info = st.text_input("Updated Contact Info")
    updated_industry = st.text_input("Updated Industry")
    updated_profile_status = st.selectbox("Updated Profile Status", [0, 1], format_func=lambda x: "Inactive" if x == 0 else "Active")

    submitted = st.form_submit_button("Update Employer")
    if submitted:
        if not updated_name or not updated_contact_info:
            st.error("Name and Contact Info are required for updates.")
        else:
            # Build the payload
            update_payload = {
                "name": updated_name,
                "contact_info": updated_contact_info,
                "industry": updated_industry,
                "profile_status": updated_profile_status,
            }

            try:
                # Send PUT request to update the employer
                update_response = requests.put(f"{API_URL}/{employer_id_to_update}", json=update_payload)
                if update_response.status_code == 200:
                    st.success("Employer updated successfully!")
                elif update_response.status_code == 404:
                    st.error("Employer not found.")
                else:
                    st.error(f"Failed to update employer: {update_response.text}")
            except Exception as e:
                st.error(f"Error: {e}")

# Delete Employer
st.write("---")
st.subheader("Delete Employer")

with st.form("delete_employer_form"):
    employer_id_to_delete = st.number_input("Enter Employer ID to Delete", min_value=1, step=1)

    delete_submitted = st.form_submit_button("Delete Employer")
    if delete_submitted:
        try:
            # Send DELETE request to delete the employer
            delete_response = requests.delete(f"{API_URL}/{employer_id_to_delete}")
            if delete_response.status_code == 200:
                st.success("Employer deleted successfully!")
            elif delete_response.status_code == 404:
                st.error("Employer not found.")
            else:
                st.error(f"Failed to delete employer: {delete_response.text}")
        except Exception as e:
            st.error(f"Error: {e}")