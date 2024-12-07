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
        'Resource_Allocation_ID', 'Resource_Type', 'Metrics_Name', 'Student_ID', 
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

    # Calculate Metrics
    total_students = director_dashboard['Student_ID'].nunique()
    total_job_positions = director_dashboard['Resource_Allocation_ID'].nunique()
    placed_students = director_dashboard[director_dashboard['Student_Program'].notna()]['Student_ID'].nunique()
    placement_rate = (placed_students / total_students * 100) if total_students > 0 else 0
    avg_feedback_length = director_dashboard['Employer_Feedback'].dropna().apply(len).mean() if 'Employer_Feedback' in director_dashboard else 0
    program_growth_metrics = director_dashboard['Metrics_Name'].nunique()

    # Display Metrics
    st.write('')
    st.write('')
    st.subheader("Program Metrics Summary")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Students", total_students)
        st.metric("Placed Students", placed_students)
    with col2:
        st.metric("Total Job Positions", total_job_positions)
        st.metric("Placement Rate (%)", round(placement_rate, 2))
    with col3:
        st.metric("Avg Feedback Length", f"{round(avg_feedback_length, 2)} letters")
        st.metric("Program Growth Metrics", program_growth_metrics)

    # Create Bar Chart for Visualization
    st.write('')
    st.write('')
    st.subheader("Metric Visualization")
    metrics_data = pd.DataFrame({
        'Metric': [
            'Total Students', 'Total Job Positions', 'Placed Students',
            'Placement Rate', 'Avg Feedback Length', 'Program Growth Metrics'
        ],
        'Value': [
            total_students, total_job_positions, placed_students,
            round(placement_rate, 2), round(avg_feedback_length, 2), program_growth_metrics
        ]
    })

    st.bar_chart(metrics_data.set_index('Metric'), horizontal=True)

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching data: {e}")

# Update Director Data
st.write('')
st.write('')
st.subheader("Update Director Information")
director_id = st.number_input("Director ID", min_value=1, step=1)
updated_name = st.text_input("Updated Name")
updated_contact_info = st.text_input("Updated Contact Info")
updated_resource_type = st.text_input("Updated Resource Type")
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
