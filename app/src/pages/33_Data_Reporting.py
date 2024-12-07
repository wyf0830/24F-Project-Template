import streamlit as st
import requests
import pandas as pd
from modules.nav import SideBarLinks

# Sidebar navigation
SideBarLinks()

# Set page title
st.title("Advisor: Manage Student Data")

# API Endpoints
API_URL = "http://api:4000/ad/student_data"

# Section: View Students
st.subheader("View Student Information")

try:
    response = requests.get(API_URL)
    response.raise_for_status()

    # Convert JSON response to DataFrame
    students_data = response.json()

    # Desired column order for display
    desired_order = [
        "Advisor_ID", "Advisor_Name", "Advisor_Contact", 
        "Student_ID", "Student_Name", "Student_Major", 
        "Student_Profile_Status", "Student_Program"
    ]

    if students_data:
        students_df = pd.DataFrame(students_data)

        # Reorder columns based on the desired order
        missing_columns = [col for col in desired_order if col not in students_df.columns]
        if missing_columns:
            st.error(f"The following columns are missing from the data: {missing_columns}")
        else:
            students_df = students_df[desired_order]

        # Display the DataFrame
        st.dataframe(students_df)
    else:
        st.warning("No student data available.")

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching student data: {e}")

st.write("---")

with st.form("add_student_form"):
    student_name = st.text_input("Student Name", help="Enter the student's full name")
    student_major = st.text_input("Student Major", help="Enter the student's major")
    student_program = st.text_input("Student Program", help="Enter the student's program (e.g., Undergraduate, Graduate)")
    student_status = st.selectbox("Student Profile Status", options=[1, 0], format_func=lambda x: "Active" if x == 1 else "Inactive")
    submit_add = st.form_submit_button("Add Student")

if submit_add:
    if student_name and student_major and student_program:
        payload = {
            "Student_Name": student_name,
            "Student_Major": student_major,
            "Student_Program": student_program,
            "Student_Profile_Status": student_status
        }
        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 201:
                st.success("Student added successfully!")
            else:
                st.error(f"Failed to add student. Error: {response.json().get('error', 'Unknown error')}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to the server: {e}")
    else:
        st.error("All fields are required to add a student.")

st.write("---")

# Section: Update Student
st.subheader("Update Student Information")

with st.form("update_student_form"):
    student_id = st.number_input("Student ID", min_value=1, step=1, help="Enter the student ID to update")
    updated_name = st.text_input("Updated Student Name")
    updated_major = st.text_input("Updated Student Major")
    updated_program = st.text_input("Updated Student Program")
    updated_status = st.selectbox("Updated Profile Status", options=[1, 0], format_func=lambda x: "Active" if x == 1 else "Inactive")
    submit_update = st.form_submit_button("Update Student")

if submit_update:
    if student_id and updated_name and updated_major and updated_program:
        payload = {
            "Student_Name": updated_name,
            "Student_Major": updated_major,
            "Student_Program": updated_program,
            "Student_Profile_Status": updated_status
        }
        try:
            response = requests.put(f"{API_URL}/{student_id}", json=payload)
            if response.status_code == 200:
                st.success("Student information updated successfully!")
            elif response.status_code == 404:
                st.error("Student not found.")
            else:
                st.error(f"Failed to update student. Error: {response.json().get('error', 'Unknown error')}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to the server: {e}")
    else:
        st.error("All fields are required to update student information.")

st.write("---")

# Section: Delete Student
st.subheader("Delete Student")

with st.form("delete_student_form"):
    delete_student_id = st.number_input("Student ID to Delete", min_value=1, step=1, help="Enter the student ID to delete")
    submit_delete = st.form_submit_button("Delete Student")

if submit_delete:
    if delete_student_id:
        try:
            response = requests.delete(f"{API_URL}/{delete_student_id}")
            if response.status_code == 200:
                st.success("Student deleted successfully!")
            elif response.status_code == 404:
                st.error("Student not found.")
            else:
                st.error(f"Failed to delete student. Error: {response.json().get('error', 'Unknown error')}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to the server: {e}")
    else:
        st.error("Student ID is required to delete a student.")