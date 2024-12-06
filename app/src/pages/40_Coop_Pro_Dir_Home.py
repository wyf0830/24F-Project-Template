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
if st.button('View Data Dashboard', type='primary', use_container_width=True):
    st.switch_page('pages/41_Data_Dashboard.py')

if st.button('Program Impact Reports', type='primary', use_container_width=True):
    st.switch_page('pages/42_Program_Impact_Reports.py')

if st.button('Employer Partnership Analysis', type='primary', use_container_width=True):
    st.switch_page('pages/43_Employer_Partnership_Analysis.py')