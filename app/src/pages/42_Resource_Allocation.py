import streamlit as st

st.set_page_config(page_title="Resource Allocation Insights", layout="wide")

st.title("Resource Allocation Insights")
st.write("Analyze resource allocation to optimize program performance.")

# 示例图表（假设使用 matplotlib 或其他图表库）
st.write("#### Current Resource Allocation by Program")
st.bar_chart({
    "Program A": 60,
    "Program B": 20,
    "Program C": 30,
    "Program D": 50
})

st.write("#### Recommendations")
st.write("- Allocate additional resources to **Program B** due to increasing demand.")
st.write("- Reduce resources from underperforming areas to support high-impact programs.")
