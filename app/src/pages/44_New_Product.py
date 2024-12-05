import streamlit as st

st.set_page_config(page_title="Add New Product", layout="wide")

st.title("Add New Product")
st.write("This page allows you to add new products to the inventory.")
# 示例内容
product_name = st.text_input("Enter the product name:")
product_category = st.selectbox("Select a category:", ["Stationery", "Electronics", "Furniture"])
product_quantity = st.number_input("Enter the quantity:", min_value=0, step=1)

if st.button("Add Product"):
    if product_name and product_category:
        st.success(f"Product '{product_name}' added under category '{product_category}' with quantity {product_quantity}!")
    else:
        st.error("Please fill in all fields.")

