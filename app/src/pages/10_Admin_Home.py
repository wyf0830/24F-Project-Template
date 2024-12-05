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
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Update Employer Information', type='primary', use_container_width=True):
        st.switch_page('00_Update_Employer')

with col2:
    if st.button('View Automated Alerts', type='primary', use_container_width=True):
        st.switch_page('pages/10_Automated_Alerts')

with col3:
    if st.button('Data Cleanup', type='primary', use_container_width=True):
        st.switch_page('pages/20_Data_Cleanup')

st.write('')
st.write('')
col4, col5, col6 = st.columns(3)

with col1:
    if st.button('Bulk Data Import', type='primary', use_container_width=True):
        st.switch_page('pages/30_Bulk_Data_Import')

with col2:
    if st.button('Scheduled Backups', type='primary', use_container_width=True):
        st.switch_page('pages/40_Scheduled_Backups')

with col3:
    if st.button('Generate Automated Reports', type='primary', use_container_width=True):
        st.switch_page('pages/50_Automated_Reports')