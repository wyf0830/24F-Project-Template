# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")

#### ------------------------ System Admin Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/10_Admin_Home.py", label="System Admin Home Page", icon="🖥️")

def ViewEmpNav():
    st.sidebar.page_link("pages/11_Update_Employer.py", label="View Employer Information", icon="👔")

def ManageEmpNav():
    st.sidebar.page_link("pages/12_Remove_Employer.py", label="Manage Employer Information", icon="💼")

def AdminDashboardNav():
    st.sidebar.page_link("pages/13_Admin_Dashboard.py", label="Admin Dashboard", icon="📊")

#### ------------------------ Student Role ------------------------
def StudentPafeNav():
    st.sidebar.page_link("pages/10_NEU_student_Home.py", label="Student Home Page", icon="🧑‍🎓")

def ProfileInfoNav():
    st.sidebar.page_link("pages/14_Profile_Information.py", label="Profile Information", icon="🖥️")

def SatisfictionPreNav():
    st.sidebar.page_link("pages/11_Prediction.py", label="Satisfiction Information", icon="🩵")

def PositionFilterNav():
    st.sidebar.page_link("pages/12_Job_Filter.py", label="Position Filter", icon="💼")

def ClassificationNav():
    st.sidebar.page_link("pages/13_Classification.py", label="Position Classification", icon="📉")

### ------------------------ Advisor Role ------------------------
def AdvisorHomeNav():
    st.sidebar.page_link("pages/30_Coop_Advisor_Home.py", label="Advisor Home", icon="👤")

def SearchStuNav():
    st.sidebar.page_link("pages/31_View_Student_Profiles.py", label="Search Student Profile", icon="🧑‍🎓")

def SearchStuFeedNav():
    st.sidebar.page_link("pages/32_Feedback.py", label="Search Student's Employer Feedback", icon="💼")

def AdvisorManageNav():
    st.sidebar.page_link("pages/33_Data_Reporting.py", label="Manage Student Information", icon="📊")

### ------------------------ Program Director Role ------------------------
def DirectorHomeNav():
    st.sidebar.page_link("pages/40_Coop_Pro_Dir_Home.py", label="Program Director Home", icon="👤")

def DataDashboardNav():
    st.sidebar.page_link("pages/41_Data_Dashboard.py", label="Data Dashboard", icon="📊")

def PerformanceNav():
    st.sidebar.page_link("pages/42_Program_Performance_Reports.py", label="Program Performance Report", icon="🏆")

def EmpAnalysisNav():
    st.sidebar.page_link("pages/43_Employer_Partnership_Analysis.py", label="Employer Partnership Analysis", icon="💼")

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # If the user is an administrator, give them access to the administrator pages
        if st.session_state["role"] == "administrator":
            AdminPageNav()
            ViewEmpNav()
            ManageEmpNav()
            AdminDashboardNav()

        # If the user role is student, show the Api Testing page
        if st.session_state['role'] == 'students':
            StudentPafeNav()
            ProfileInfoNav()
            SatisfictionPreNav()
            PositionFilterNav()
            ClassificationNav()

        # If the user role is program director, show the Api Testing page
        if st.session_state['role'] == 'advisor':
            AdvisorHomeNav()
            SearchStuNav()
            SearchStuFeedNav()
            AdvisorManageNav()
        
        # If the user role is program director, show the Api Testing page
        if st.session_state['role'] == 'program_director':
            DirectorHomeNav()
            DataDashboardNav()
            PerformanceNav()
            EmpAnalysisNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
