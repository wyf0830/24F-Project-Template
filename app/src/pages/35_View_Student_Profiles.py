import streamlit as st

st.set_page_config(page_title="View Student Profiles", layout="wide")

st.title("View Student Profiles")
st.write("Access detailed profiles of students to assist in career guidance.")

# Example student data
students = [
    {"name": "Alice Johnson", "skills": "Python, Data Analysis", "goals": "Data Scientist"},
    {"name": "Bob Smith", "skills": "Java, Cloud Computing", "goals": "Backend Developer"}
]

# Display student profiles
for student in students:
    st.subheader(student["name"])
    st.write(f"Skills: {student['skills']}")
    st.write(f"Career Goals: {student['goals']}")
    st.write("---")
    