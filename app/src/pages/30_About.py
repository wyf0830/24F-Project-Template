import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    Introducing Expeduco, a cutting-edge, data-driven platform designed
      to revolutionize the co-op and internship experience at Northeastern University.
        Expeduco streamlines the connection between students and employers by leveraging
          advanced data analytics to provide personalized co-op recommendations, real-time 
          application tracking, and insightful program performance metrics. In an era where
            manual updates, system inefficiencies, and generic job listings hinder progress, 
            Expeduco emerges as a solution that not only saves time but also enhances the 
            quality of matches between students and employers.
    """
        )

if st.button('Back to home page', type='primary', use_container_width=True):
  st.switch_page('Home.py')