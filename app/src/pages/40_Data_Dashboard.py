import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Data Dashboard')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")

try:
    # Access /p/categories with a GET request
    director_dashboard_response = requests.get('http://web-api:4000/d/data_dashboard')
    
    # 200 means the request was successful
    if director_dashboard_response.status_code == 200:
        # pull the data from the response object as json
        director_data = director_dashboard_response.json()
    else:
        # means we got back some HTTP code besides 200
        st.error("Failed to fetch categories")
except requests.exceptions.RequestException as e:
    st.error(f"Error connecting to director API: {str(e)}")