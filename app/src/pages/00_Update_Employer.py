import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks

# Initialize the navigation links
SideBarLinks()

# Define API URL for employers data
API_URL = 'http://api:4000/a/employers'

st.title("Update Employer Information")

# Fetch and Display Employers Data
st.subheader("Employer List")

try:
    # Fetch data from the API
    response = requests.get(API_URL)
    response.raise_for_status()  # Raise an error for bad responses
    employer_data = response.json()

    # Convert JSON response to Pandas DataFrame
    employer_df = pd.DataFrame(employer_data)

    # Define the desired column order
    desired_order = ['Employer_ID', 'Name', 'Industry', 'Contact_Info', 'Profile_Status']

    # Check if all desired columns exist in the data
    missing_columns = [col for col in desired_order if col not in employer_df.columns]
    if missing_columns:
        st.error(f"The following columns are missing in the data: {missing_columns}")
    else:
        # Reorder the columns
        employer_df = employer_df[desired_order]

        # Display the data
        st.dataframe(employer_df)

        # Metrics: Total Employers
        st.write("---")
        total_employers = len(employer_df)
        st.metric("Total Employers", total_employers)

         # Metric: Most Frequent Industry
        most_frequent_industry = employer_df['Industry'].mode()[0]  # Get the most common industry
        industry_count = employer_df['Industry'].value_counts().iloc[0]  # Count occurrences of the most common industry
        st.metric("Most Frequent Industry", most_frequent_industry, f"{industry_count} Employers")

        # Optional: Add filters or sorting
        st.write("---")
        st.subheader("Filter Employers")
        industries = employer_df['Industry'].dropna().unique()
        selected_industry = st.selectbox("Select Industry", options=["All"] + list(industries))

        if selected_industry != "All":
            filtered_df = employer_df[employer_df['Industry'] == selected_industry]
        else:
            filtered_df = employer_df

        st.dataframe(filtered_df)

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching employer data: {e}")

# Add Employer
st.write("---")
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