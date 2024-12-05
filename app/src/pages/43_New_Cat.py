import streamlit as st

st.set_page_config(page_title="Add New Product Category", layout="wide")

st.title("Add New Product Category")
st.write("This page allows you to add new product categories.")
# 示例内容
category_name = st.text_input("Enter the new category name:")
if st.button("Add Category"):
    if category_name:
        st.success(f"New category '{category_name}' added successfully!")
    else:
        st.error("Please enter a valid category name.")
