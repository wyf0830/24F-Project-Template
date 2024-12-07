import streamlit as st

st.set_page_config(page_title="Employer Feedback Tracking", layout="wide")

st.title("Employer Feedback Tracking")
st.write("Track feedback from employers for student applications.")

# example feedback data
feedback = {
    "Alice Johnson": "Excellent technical skills, invited for the next round.",
    "Bob Smith": "Lacks experience in cloud computing."
}

st.write("### Employer Feedback")
for student, comment in feedback.items():
    st.subheader(student)
    st.write(f"**Feedback:** {comment}")
    st.write("---")

