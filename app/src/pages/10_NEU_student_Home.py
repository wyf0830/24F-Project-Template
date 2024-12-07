import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')


#TODO change all the buttons below, match the persona
if st.button('Profile Information', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Profile_Information.py')

if st.button('Satisfiction Prediction', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Prediction.py')

if st.button('Position Filter', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Job_Filter.py')

if st.button("Job Classification Demo",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Classification.py')