import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

st.title("khoury advisor portal")

st.subheader("Recent trends on available jobs")
# TODO change below
col1, col2 = st.columns(2)
with col1:
    if st.button("Show All Reorders", type='primary', use_container_width=True):
        st.switch_page("pages/41_Reorders.py")
with col2:
    if st.button("Show Low Stock", type='primary', use_container_width=True):
        st.switch_page("pages/42_Low_Stock.py")

st.subheader("New job offers")
# TODO change below
col3, col4 = st.columns(2)
with col3:
    if st.button("Add New Product Category", type='primary', use_container_width=True):
        st.switch_page("pages/43_New_Cat.py")
with col4:
    if st.button("Add New Product", type='primary', use_container_width=True):
        st.switch_page("pages/44_New_Product.py")
