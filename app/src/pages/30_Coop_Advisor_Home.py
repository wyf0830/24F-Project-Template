# app/src/pages/30_Coop_Advisor_Home.py

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(page_title="Career Advisor Dashboard", layout="wide")

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

st.title(f"Welcome, {st.session_state['first_name']}.")

st.write('')
st.write('')
st.write('### What would you like to do today?')

# Navigation buttons
if st.button('Search Student Profiles', type='primary', use_container_width=True):
    st.switch_page('pages/31_View_Student_Profiles.py')

if st.button('Search Employer Feedback', type='primary', use_container_width=True):
    st.switch_page('pages/32_Feedback.py')

if st.button('Manage Student Data', type='primary', use_container_width=True):
    st.switch_page('pages/33_Data_Reporting.py')

if st.button('Employer Feedback Tracking', type='primary', use_container_width=True):
    st.switch_page('pages/34_Feedback_Tracking')