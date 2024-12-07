import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    Expeduco is a state-of-the-art, data-driven platform meticulously designed to transform the cooperative education (co-op) and internship experience at Northeastern University. With its innovative approach, Expeduco serves as a bridge between students and employers, redefining the way connections are established and nurtured.
    
    Leveraging the power of advanced data analytics, Expeduco offers a comprehensive suite of features, including personalized co-op recommendations tailored to individual student preferences, real-time tracking of applications to ensure transparency and efficiency, and detailed program performance metrics to provide actionable insights for continuous improvement.
    
    In today's fast-paced world, where outdated systems, manual updates, and generic job listings often create bottlenecks and hinder meaningful progress, Expeduco rises as a beacon of innovation. By automating processes, optimizing matches between students and employers, and focusing on data-backed decision-making, the platform not only saves significant time for all stakeholders but also elevates the overall quality of the co-op and internship experience. Expeduco empowers students to unlock their potential and helps employers discover the right talent efficiently, fostering a mutually beneficial ecosystem that drives success for all.
    """
        )

if st.button('Back to home page', type='primary', use_container_width=True):
  st.switch_page('Home.py')