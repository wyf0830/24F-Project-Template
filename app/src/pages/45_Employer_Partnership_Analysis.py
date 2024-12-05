import streamlit as st

st.set_page_config(page_title="Employer Partnership Analysis", layout="wide")

st.title("Employer Partnership Analysis")
st.write("Analyze and strengthen employer partnerships.")

# 示例合作分析
st.write("#### Current Employer Engagement Levels")
st.bar_chart({
    "Employer A": 30,
    "Employer B": 50,
    "Employer C": 40,
    "Employer D": 20
})

st.write("#### Suggestions for Improvement")
st.write("- Strengthen partnerships with **Employer C** through targeted outreach.")
st.write("- Expand collaboration with employers in emerging industries.")
