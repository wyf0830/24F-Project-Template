# `modules` Folder

Currently, we are using this folder to hold functionality that needs to be accessible to the entire application. `nav.py` is a module that supports our custom navigation bar on the left of the app along with some basic Role-Based Access Control (RBAC). 


###

1. Function Overview
nav.py is the core navigation module of this project, mainly used for:

Dynamically generate the left sidebar navigation of the Streamlit application.
Display personalized pages based on user roles (e.g. pol_strat_advisor, usaid_worker, administrator, etc.).
Support basic Role-Based Access Control (RBAC).
Provide global common links (e.g. Home and About pages).


2. Module Structure
The file contains the following main elements:

- Generic page navigation:
HomeNav(): add a link to the home page.
AboutPageNav(): link added to the about page.

- Role-specific page navigation:
PolStratAdvHomeNav(): home page of the political strategy advisor.
AdminPageNav(): administrator specific page.
More navigation functions correspond to role-specific pages.

- Global navigation functions:
SideBarLinks(show_home=False): dynamically renders the sidebar navigation content according to the user's role, providing a unified interface call.

* Usage instructions
- Call the SideBarLinks function: Import the module in the page file where the navigation bar is to be generated and call the:
'''
import nav
nav.SideBarLinks(show_home=True)
'''

- Restart or refresh the app: After saving your changes, refresh the Streamlit app page to see the updated sidebar navigation.