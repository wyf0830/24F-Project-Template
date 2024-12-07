import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks


SideBarLinks()

# API URL for students
API_URL = 'http://api:4000/s/students'

st.title("Manage Student Information")

# Fetch and Display Students
st.subheader("Student List")

try:
    # Getting data from the API
    response = requests.get(API_URL)
    response.raise_for_status()  # Raise an error for bad responses
    student_data = response.json()

    # Convert JSON response to Pandas DataFrame
    student_df = pd.DataFrame(student_data)

    if not student_df.empty:
        # Define the desired column order
        desired_order = ['Student_ID', 'Name', 'Major', 'Interests', 'Program', 'Profile_Status']
        student_df = student_df[desired_order]

        # Display the student data in a table
        st.dataframe(student_df)
    else:
        st.error("No student data available.")

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching student data: {e}")

# Add Student
st.write("---")
st.subheader("Add Student")
name = st.text_input("Name")
major = st.text_input("Major")
interests = st.text_input("Interests")
program = st.text_input("Program")
profile_status = st.selectbox("Profile Status", [0, 1], format_func=lambda x: "Inactive" if x == 0 else "Active")

if st.button("Add Student"):
        payload = {
            "Name": name,
            "Major": major,
            "Interests": interests,
            "Program": program,
            "Profile_Status": profile_status,
        }
        try:
            post_response = requests.post(API_URL, json=payload)
            if post_response.status_code == 201:
                st.success("Student added successfully!")
            else:
                # Attempt to extract error message from response
                try:
                    error_info = post_response.json()
                    error_message = error_info.get('error', 'Unknown error.')
                except ValueError:
                    error_message = post_response.text
                st.error(f"Failed to add Student. Status Code: {post_response.status_code}\nResponse: {error_message}")
        except Exception as e:
            st.error(f"Error: {e}")

# Update Student
st.write("---")
st.subheader("Update Student")

with st.form("update_student_form"):
    student_id_to_update = st.number_input("Enter Student ID to Update", min_value=1, step=1)
    updated_name = st.text_input("Updated Name")
    updated_major = st.text_input("Updated Major")
    updated_interests = st.text_input("Updated Interests")
    updated_program = st.text_input("Updated Program")
    updated_profile_status = st.selectbox("Updated Profile Status", [0, 1], format_func=lambda x: "Inactive" if x == 0 else "Active")

    submitted = st.form_submit_button("Update Student")
    if submitted:

            # Build the payload
            update_payload = {
                "name": updated_name,
                "major": updated_major,
                "industry": updated_interests,
                "program": updated_program,
                "profile_status": updated_profile_status,
            }

            try:
                # Send PUT request to update the student
                update_response = requests.put(f"{API_URL}/{student_id_to_update}", json=update_payload)
                if update_response.status_code == 200:
                    st.success("Student updated successfully!")
                elif update_response.status_code == 404:
                    st.error("Student not found.")
                else:
                    st.error(f"Failed to update student: {update_response.text}")
            except Exception as e:
                st.error(f"Error: {e}")

# Delete Student
st.write("---")
st.subheader("Delete Student")

with st.form("delete_student_form"):
    student_id_to_delete = st.number_input("Enter Student ID to Delete", min_value=1, step=1)

    delete_submitted = st.form_submit_button("Delete Student")
    if delete_submitted:
        try:
            # Send DELETE request to delete the student
            delete_response = requests.delete(f"{API_URL}/{student_id_to_delete}")
            if delete_response.status_code == 200:
                st.success("Student deleted successfully!")
            elif delete_response.status_code == 404:
                st.error("Student not found.")
            else:
                st.error(f"Failed to delete student: {delete_response.text}")
        except Exception as e:
            st.error(f"Error: {e}")