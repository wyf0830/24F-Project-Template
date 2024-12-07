# app/src/pages/10_Admin_Home.py

import logging
import streamlit as st
from modules.nav import SideBarLinks

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

st.set_page_config(page_title="Co-op Admin Dashboard", layout="wide")

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

# Welcome Message
st.title(f"Welcome, {st.session_state.get('first_name', 'Admin')}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

# Navigation Buttons
if st.button('View Employer Information', type='primary', use_container_width=True):
    st.switch_page('pages/11_Update_Employer.py')

if st.button('Manage Employer Information', type='primary', use_container_width=True):
    st.switch_page('pages/12_Remove_Employer.py')

if st.button('Admin Dashboard', type='primary', use_container_width=True):
    st.switch_page('pages/13_Admin_Dashboard.py')