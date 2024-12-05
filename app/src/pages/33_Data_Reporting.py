import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Reporting", layout="wide")

st.title("Data Reporting")
st.write("Analyze student application success rates and market trends.")


# Example data
students = ["Alice Johnson", "Bob Smith", "Charlie Brown"]
success_rates = [80, 60, 70]
# Create a bar chart
fig, ax = plt.subplots()
ax.bar(students, success_rates, color="skyblue")
ax.set_title("Student Application Success Rates")
ax.set_ylabel("Success Rate (%)")
ax.set_xlabel("Students")

st.pyplot(fig)