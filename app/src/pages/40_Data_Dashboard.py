import streamlit as st

st.set_page_config(page_title="Data Dashboard", layout="wide")

st.title("Data Dashboard")
st.write("Visualize and analyze key data metrics related to program performance.")

# 示例数据展示
st.write("#### Key Metrics Overview")
st.bar_chart({
    "Metric A": [10, 20, 30],
    "Metric B": [15, 25, 35],
    "Metric C": [20, 30, 40],
})

st.write("#### Data Insights")
st.write("- Metric A has shown consistent growth.")
st.write("- Metric B requires further analysis to determine trends.")
