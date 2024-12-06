import logging
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from modules.nav import SideBarLinks

SideBarLinks()

st.title("Job Classification")

st.write("### Predict Suitable Job Category")

st.write(
    "Provide your skills and preferences, and the app will predict the most suitable job category for you!"
)

# User input for skills and preferences
st.sidebar.header("User Input Parameters")

def user_input_features():
    skill_level = st.sidebar.slider("Skill Level (1-10)", 1, 10, 5)
    communication_level = st.sidebar.slider("Communication Level (1-10)", 1, 10, 5)
    leadership = st.sidebar.slider("Leadership (1-10)", 1, 10, 5)
    adaptability = st.sidebar.slider("Adaptability (1-10)", 1, 10, 5)
    data = {
        "skill_level": skill_level,
        "communication_level": communication_level,
        "leadership": leadership,
        "adaptability": adaptability,
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader("User Input Parameters")
st.write(df)

# Simulate a classifier
categories = ["Software Engineer", "Manager", "Data Scientist", "Salesperson"]
clf = RandomForestClassifier()
X = pd.DataFrame([
    [8, 7, 6, 7],  # Software Engineer
    [5, 8, 8, 6],  # Manager
    [9, 6, 5, 7],  # Data Scientist
    [6, 9, 7, 8],  # Salesperson
], columns=["skill_level", "communication_level", "leadership", "adaptability"])
y = [0, 1, 2, 3]
clf.fit(X, y)

# Predict the job category
prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader("Prediction")
st.write(f"Recommended Job: {categories[prediction[0]]}")

st.subheader("Prediction Probability")
st.write(pd.DataFrame(prediction_proba, columns=categories))
