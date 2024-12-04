##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# import the main streamlit library as well
# as SideBarLinks function from src/modules folder
import streamlit as st
from modules.nav import SideBarLinks

# streamlit supports reguarl and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout = 'wide')

# If a user is at this page, we assume they are not 
# authenticated.  So we change the 'authenticated' value
# in the streamlit session_state to false. 
st.session_state['authenticated'] = False

# Use the SideBarLinks function from src/modules/nav.py to control
# the links displayed on the left-side panel. 
# IMPORTANT: ensure src/.streamlit/config.toml sets
# showSidebarNavigation = false in the [client] section
SideBarLinks(show_home=True)

# ***************************************************
#    The major content of this page
# ***************************************************

# set the title of the page and provide a simple prompt. 
logger.info("Loading the Home page of the app")
st.title('Welcome to Expeduco!')
st.write('\n\n')
st.write('### As which user would you like to log in?')

# For each of the user personas for which we are implementing
# functionality, we put a button on the screen that the user 
# can click to MIMIC logging in as that mock user. 
#TODO 这些注释和老师写template的最后再删
if st.button("Act as John, a Political Strategy Advisor", 
            type = 'primary', 
            use_container_width=True):
    # when user clicks the button, they are now considered authenticated
    st.session_state['authenticated'] = True
    # we set the role of the current user
    st.session_state['role'] = 'pol_strat_advisor'
    # we add the first name of the user (so it can be displayed on 
    # subsequent pages). 
    st.session_state['first_name'] = 'John'
    # finally, we ask streamlit to switch to another page, in this case, the 
    # landing page for this particular user type
    logger.info("Logging in as Political Strategy Advisor Persona")
    st.switch_page('pages/00_Pol_Strat_Home.py')

if st.button('Act as David Chen, System Administrator', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'administrator'
    st.session_state['first_name'] = 'SysAdmin'
    st.switch_page('pages/10_Admin_Home.py')

if st.button('Act as Steven Johnson, senior student at neu', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
<<<<<<< HEAD
    st.session_state['role'] = 'student'
    st.session_state['first_name'] = 'Steven'
    st.switch_page('pages/10_NEU_student_Home.py')
=======
    st.session_state['role'] = 'Coop seeker'
    st.session_state['first_name'] = 'David'
    st.switch_page('pages/20_Coop_Seeker_Home.py')
>>>>>>> b35c005cddb8f319a9b32a8930edbabc22a43930

if st.button('Act as Michael Lee, khoury advisor', 
             type='primary', 
             use_container_width=True):
    st.session_state['authenticated'] = True
<<<<<<< HEAD
    st.session_state['role'] = 'khoury advisor'
    st.switch_page('pages/40_Khoury_Advisor_Portal.py')
=======
    st.session_state['role'] = 'Coop advisor'
    st.session_state['first_name'] = 'Michael'
    st.switch_page('pages/30_Coop_Advisor_Home.py')
>>>>>>> b35c005cddb8f319a9b32a8930edbabc22a43930

if st.button('Act as Hiroshi Saito, Co-op Program Director',
             type = 'primary',
             use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'Program Director'
    st.session_state['first_name'] = 'Hiroshi'
    st.switch_page('pages/40_Coop_Pro_Dir_Home.py')
    



