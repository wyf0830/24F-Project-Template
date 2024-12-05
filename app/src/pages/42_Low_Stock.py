import streamlit as st

st.set_page_config(page_title="Low Stock", layout="wide")

st.title("Low Stock Items")
st.write("This page displays items with low stock levels.")
# 示例内容
low_stock_items = [
    {"Item": "Paper", "Stock": 5, "Restock Needed": "Yes"},
    {"Item": "Stapler", "Stock": 2, "Restock Needed": "Yes"},
    {"Item": "Eraser", "Stock": 0, "Restock Needed": "Yes"},
]

st.table(low_stock_items)

