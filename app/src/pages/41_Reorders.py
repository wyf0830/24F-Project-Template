import streamlit as st

st.set_page_config(page_title="Reorders", layout="wide")

st.title("Reorders")
st.write("This is the Reorders page.")
st.write("Here you can view all reorders for items that need to be restocked.")
# 示例内容
reorders = [
    {"Item": "Notebook", "Quantity": 20, "Supplier": "ABC Supplies"},
    {"Item": "Pen", "Quantity": 50, "Supplier": "Stationery Co."},
    {"Item": "Marker", "Quantity": 10, "Supplier": "Markers Ltd."},
]

st.table(reorders)
