# app/src/pages/40_Coop_Pro_Dir_Home.py

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(page_title="Program Director Dashboard", layout="wide")

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

st.title(f"Welcome, {st.session_state['first_name']}.")

st.write('')
st.write('')
st.write('### What would you like to do today?')

# Navigation buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('View Data Dashboard', type='primary', use_container_width=True):
        st.switch_page('pages/40_Data_Dashboard')

with col2:
    if st.button('Real-Time Metrics Tracking', type='primary', use_container_width=True):
        st.switch_page('pages/41_RealTime_Metrics')

with col3:
    if st.button('Resource Allocation Insights', type='primary', use_container_width=True):
        st.switch_page('pages/42_Resource_Allocation')

st.write('')
st.write('')
col4, col5, col6 = st.columns(3)

with col1:
    if st.button('Trends and Patterns Analysis', type='primary', use_container_width=True):
        st.switch_page('pages/43_Trends_Analysis')

with col2:
    if st.button('Program Impact Reports', type='primary', use_container_width=True):
        st.switch_page('pages/44_Program_Impact_Reports')

with col3:
    if st.button('Employer Partnership Analysis', type='primary', use_container_width=True):
        st.switch_page('pages/45_Employer_Partnership_Analysis')