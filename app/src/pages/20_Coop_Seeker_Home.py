# app/src/pages/20_Coop_Seeker_Home.py

import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

# Navigation buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Create/Update Profile', type='primary', use_container_width=True):
        st.switch_page('pages/20_Create_Profile')

with col2:
    if st.button('View Recommendations', type='primary', use_container_width=True):
        st.switch_page('pages/21_Receive_Recommendations')

with col3:
    if st.button('Track Applications', type='primary', use_container_width=True):
        st.switch_page('pages/22_Track_Applications')

st.write('')
st.write('')
col4, col5, col6 = st.columns(3)

with col1:
    if st.button('Edit Files', type='primary', use_container_width=True):
        st.switch_page('pages/24_File_Editing')

with col2:
    if st.button('View Notifications', type='primary', use_container_width=True):
        st.switch_page('pages/25_Notifications')

with col3:
    if st.button('Update Profile', type='primary', use_container_width=True):
        st.switch_page('pages/23_Update_Profile')