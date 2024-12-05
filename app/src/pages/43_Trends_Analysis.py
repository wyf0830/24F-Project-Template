import streamlit as st

st.set_page_config(page_title="Trends and Patterns Analysis", layout="wide")

st.title("Trends and Patterns Analysis")
st.write("Identify trends and patterns in program performance data.")

# 示例数据趋势展示
st.write("#### Historical Trends")
st.line_chart({
    "2020": [70, 75, 80],
    "2021": [80, 85, 90],
    "2022": [85, 90, 95]
})

st.write("#### Insights from Trends")
st.write("- Steady improvement in **student placement rates** over the years.")
st.write("- Identify seasonal peaks in job postings and applications.")
