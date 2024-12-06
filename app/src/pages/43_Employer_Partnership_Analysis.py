import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks

# Initialize the navigation links
SideBarLinks()

# API endpoint for employer data
API_URL = 'http://api:4000/d/employer'

st.title("Employer Partnership Analysis")

# Section: Fetch and Display Employer Data
st.subheader("Employer Data")

try:
    # Fetch data from the API
    response = requests.get(API_URL)
    response.raise_for_status()  # Raise an error for bad responses
    employer_data = response.json()

    # Convert JSON response to Pandas DataFrame
    employer_df = pd.DataFrame(employer_data)

    # Define column order for display
    desired_columns = [
        "Director_ID", "Director_Name", "Director_Contact", 
        "Student_ID", "Student_Name", "Student_Major", "Student_Program", 
        "Job_Title", "Industry", "Employer_Feedback", "Employer_Name", "Employer_Contact" 
    ]

    # Check if desired columns exist in the data
    missing_columns = [col for col in desired_columns if col not in employer_df.columns]
    if missing_columns:
        st.error(f"Missing columns in the data: {missing_columns}")
    else:
        # Reorder and display the DataFrame
        employer_df = employer_df[desired_columns]
        st.dataframe(employer_df)

        # Basic Insights Section
        st.write('')
        st.write('')
        st.subheader("Insights from Employer Data")

        # Total employers
        total_employers = employer_df['Employer_Name'].nunique()

        # Total job positions
        total_jobs = employer_df['Job_Title'].nunique()

        # Most common industry
        common_industry = (employer_df['Industry'].value_counts().idxmax()
                           if not employer_df['Industry'].isnull().all()
                           else "No data")

        # Employer feedback analysis
        avg_feedback_length = employer_df['Employer_Feedback'].dropna().apply(len).mean()

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Employers", total_employers)
            st.metric("Most Common Industry", common_industry)

        with col2:
            st.metric("Total Job Positions", total_jobs)
            st.metric("Avg Feedback Length", f"{round(avg_feedback_length, 2)} letters")

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching employer data: {e}")