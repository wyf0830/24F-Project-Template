import streamlit as st

st.set_page_config(page_title="Real-Time Information Updates", layout="wide")

st.title("Real-Time Information Updates")
st.write("View the latest updates on student resumes, skills, and job postings.")

# Example updates
updates = [
    "Alice Johnson uploaded a new resume.",
    "New job posting: Data Scientist at Amazon.",
    "Bob Smith added 'AWS Certification' to his skills."
]

st.write("Latest Updates:")
for update in updates:
    st.write("- " + update)

