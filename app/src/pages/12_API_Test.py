import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

SideBarLinks()

st.title("Job Listings")

st.write("### Accessing Job Listings from an API")

try:
    # get job listings
    response = requests.get('http://api:4000/job/listings')
    response.raise_for_status()
    jobs = response.json()

    # allow filtering jobs by location and job type
    col1, col2 = st.columns(2)
    with col1:
        location = st.selectbox("Filter by Location", options=["All"] + list({job['location'] for job in jobs}))
    with col2:
        job_type = st.selectbox("Filter by Job Type", options=["All"] + list({job['type'] for job in jobs}))

    # apply filters
    if location != "All":
        jobs = [job for job in jobs if job['location'] == location]
    if job_type != "All":
        jobs = [job for job in jobs if job['type'] == job_type]

    # display filtered jobs
    st.write(f"Showing {len(jobs)} job(s):")
    st.table(jobs)
except Exception as e:
    st.error(f"Error retrieving job listings: {e}")

