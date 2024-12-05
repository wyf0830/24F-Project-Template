import streamlit as st
import pandas as pd
import sqlite3  # Example database connection

# Connect to the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

st.title("Update Employer Information")

# View Employer List
st.subheader("Employer List")
df = pd.read_sql_query("SELECT * FROM Employer", conn)
st.dataframe(df)

# Edit Employer Details
st.subheader("Edit Employer")
employer_id = st.selectbox("Select Employer ID", df['Employer_ID'])
new_name = st.text_input("Name")
new_contact = st.text_input("Contact Info")
new_industry = st.text_input("Industry")
if st.button("Update Employer"):
    cursor.execute("UPDATE Employer SET Name=?, Contact_Info=?, Industry=? WHERE Employer_ID=?", 
                   (new_name, new_contact, new_industry, employer_id))
    conn.commit()
    st.success("Employer updated!")

# Add New Employer
st.subheader("Add New Employer")
name = st.text_input("New Name")
contact = st.text_input("New Contact Info")
industry = st.text_input("New Industry")
if st.button("Add Employer"):
    cursor.execute("INSERT INTO Employer (Name, Contact_Info, Industry) VALUES (?, ?, ?)", 
                   (name, contact, industry))
    conn.commit()
    st.success("New employer added!")

# Delete Employer
st.subheader("Delete Employer")
delete_id = st.selectbox("Select Employer ID to Delete", df['Employer_ID'])
if st.button("Delete Employer"):
    cursor.execute("DELETE FROM Employer WHERE Employer_ID=?", (delete_id,))
    conn.commit()
    st.success("Employer deleted!")
