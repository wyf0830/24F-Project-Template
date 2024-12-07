import logging
import streamlit as st
from modules.nav import SideBarLinks

# Logging setup
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Set page configuration
st.set_page_config(layout="wide", page_title="Expeduco!", page_icon="🌟")

# Set background image
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
set_background("https://source.unsplash.com/1600x900/?education,technology")

# Sidebar navigation
SideBarLinks(show_home=True)

# Header Section
st.markdown(
    """
    <div style="text-align: center; padding: 20px;">
        <h1 style="font-size: 3em; font-weight: bold; margin-bottom: 0; color: #FFFFFF;">Welcome to Expeduco! 🌟</h1>
        <p style="font-size: 1.5em; margin-top: 0; color: #D3D3D3;">Choose a role to explore tailored functionality and insights</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Dropdown Menu for User Selection with Icons
st.write("### Select a user to log in:")
user_roles_with_icons = {
    "👔 John, a Political Strategy Advisor": ("pol_strat_advisor", "pages/00_Pol_Strat_Home.py"),
    "💻 David Chen, System Administrator": ("administrator", "pages/10_Admin_Home.py"),
    "🎓 Steven Johnson, senior student at NEU": ("students", "pages/10_NEU_student_Home.py"),
    "📚 Michael Lee, Khoury Advisor": ("khoury_advisor", "pages/30_Coop_Advisor_Home.py"),
    "👨‍🏫 Hiroshi Saito, Co-op Program Director": ("program_director", "pages/40_Coop_Pro_Dir_Home.py"),
}

# Create a dropdown with icons
selected_user = st.selectbox("Log in as:", list(user_roles_with_icons.keys()))

# Button to confirm the selection
if st.button("Log In"):
    # Set session state variables
    role, page = user_roles_with_icons[selected_user]
    st.session_state["authenticated"] = True
    st.session_state["role"] = role
    st.session_state["first_name"] = selected_user.split(",")[0].split(" ")[1]
    logger.info(f"Logging in as {selected_user}")
    st.switch_page(page)

# Add a separate Chatbot button for direct access
st.write("### Or directly access the Chatbot:")
if st.button("💬 Go to Chatbot"):
    st.switch_page("pages/20_Simple_Chat_Bot.py")