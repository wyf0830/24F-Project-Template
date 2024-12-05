import streamlit as st

st.set_page_config(page_title="Schedule Management", layout="wide")

st.title("Schedule Management")
st.write("Manage your tasks and appointments effectively.")

# Example tasks
tasks = [
    "Resume review with Alice Johnson at 10:00 AM",
    "Employer meeting at 2:00 PM",
    "Follow-up with Bob Smith on application status"
]

st.write("Today's Tasks:")
for task in tasks:
    st.write("- " + task)

# Add a new task
new_task = st.text_input("Add a new task:")
if st.button("Add Task"):
    st.write(f"Task added: {new_task}")
