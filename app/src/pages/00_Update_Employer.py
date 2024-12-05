import streamlit as st
import requests

API_URL = "http://localhost:5000/employers"

st.title("Update Employer Information")

# View Employers
st.subheader("Employer List")
try:
    response = requests.get(API_URL)
    employers = response.json()
    st.write(employers)
except Exception as e:
    st.error(f"Failed to fetch employers: {e}")

# Add Employer
st.subheader("Add Employer")
name = st.text_input("Name")
contact_info = st.text_input("Contact Info")
industry = st.text_input("Industry")
profile_status = st.selectbox("Profile Status", [1, 0])  # 1 for active, 0 for inactive
if st.button("Add Employer"):
    payload = {
        "name": name,
        "contact_info": contact_info,
        "industry": industry,
        "profile_status": profile_status
    }
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 201:
            st.success("Employer added successfully!")
        else:
            st.error("Failed to add employer.")
    except Exception as e:
        st.error(f"Error: {e}")

# Update Employer
st.subheader("Update Employer")
employer_id = st.number_input("Employer ID", min_value=1, step=1)
name = st.text_input("Updated Name")
contact_info = st.text_input("Updated Contact Info")
industry = st.text_input("Updated Industry")
profile_status = st.selectbox("Updated Profile Status", [1, 0])
if st.button("Update Employer"):
    payload = {
        "name": name,
        "contact_info": contact_info,
        "industry": industry,
        "profile_status": profile_status
    }
    try:
        response = requests.put(f"{API_URL}/{employer_id}", json=payload)
        if response.status_code == 200:
            st.success("Employer updated successfully!")
        else:
            st.error("Failed to update employer.")
    except Exception as e:
        st.error(f"Error: {e}")

# Delete Employer
st.subheader("Delete Employer")
delete_id = st.number_input("Employer ID to Delete", min_value=1, step=1)
if st.button("Delete Employer"):
    try:
        response = requests.delete(f"{API_URL}/{delete_id}")
        if response.status_code == 200:
            st.success("Employer deleted successfully!")
        else:
            st.error("Failed to delete employer.")
    except Exception as e:
        st.error(f"Error: {e}")
