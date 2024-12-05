import streamlit as st

st.set_page_config(page_title="Personalized Recommendations", layout="wide")

st.title("Personalized Recommendations")
st.write("Provide personalized career opportunities for students.")

# example student data
students = [
    {"name": "Alice Johnson", "skills": "Python, Data Analysis", "goals": "Data Scientist"},
    {"name": "Bob Smith", "skills": "Java, Cloud Computing", "goals": "Backend Developer"}
]


selected_student = st.selectbox("Select a student:", [s["name"] for s in students])

# display recommended jobs based on selected students

for student in students:
    if student["name"] == selected_student:
        st.write(f"**Skills:** {student['skills']}")
        st.write(f"**Career Goals:** {student['goals']}")
        st.write("**Recommended Jobs:**")
        if student["goals"] == "Data Scientist":
            st.write("- Data Scientist Intern at Google")
            st.write("- Machine Learning Intern at Microsoft")
        elif student["goals"] == "Backend Developer":
            st.write("- Backend Developer Intern at Amazon")
            st.write("- Java Developer Intern at IBM")
        break
