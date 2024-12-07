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
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('View Student Profiles', type='primary', use_container_width=True):
        st.switch_page('pages/35_View_Student_Profiles.py')

with col2:
    if st.button('Personalized Recommendations', type='primary', use_container_width=True):
        st.switch_page('pages/30_Personalized_Recommendations')

with col3:
    if st.button('Employer Feedback Tracking', type='primary', use_container_width=True):
        st.switch_page('pages/32_Feedback_Tracking')

st.write('')
st.write('')
col4, col5, col6 = st.columns(3)

with col1:
    if st.button('Real-Time Information Updates', type='primary', use_container_width=True):
        st.switch_page('pages/31_RealTime_Updates')

with col2:
    if st.button('Data Reporting', type='primary', use_container_width=True):
        st.switch_page('pages/33_Data_Reporting')

with col3:
    if st.button('Schedule Management', type='primary', use_container_width=True):
        st.switch_page('pages/34_Schedule_Management')