import logging
import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')
logger = logging.getLogger(__name__)

# display the appropriate sidebar links for the role of the logged-in user
SideBarLinks()

st.title('Job Satisfaction Prediction')

# create a 2-column layout
col1, col2 = st.columns(2)

# input fields for user experience and salary expectation
with col1:
    experience_years = st.number_input('Years of Experience:', min_value=0, max_value=50, step=1)
with col2:
    expected_salary = st.number_input('Expected Salary (in $):', min_value=0, step=1000)

# log the input data
logger.info(f'Experience Years = {experience_years}')
logger.info(f'Expected Salary = {expected_salary}')

# button to calculate satisfaction prediction
if st.button('Predict Satisfaction', type='primary', use_container_width=True):
    try:
        results = requests.get(f'http://api:4000/job/prediction/{experience_years}/{expected_salary}').json()
        st.subheader("Prediction Results")
        st.json(results)
    except Exception as e:
        st.error(f"Error fetching prediction: {e}")
