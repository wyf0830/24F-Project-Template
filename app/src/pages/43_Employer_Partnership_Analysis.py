import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from modules.nav import SideBarLinks

# Initialize the navigation links
SideBarLinks()

# API endpoint for employer data
API_URL = 'http://api:4000/d/employer'

st.title("Employer Partnership Analysis")

# Helper Function
def calculate_score(feedback):
    """
    Calculate a score for Employer Feedback based on predefined positive keywords.
    The score is calculated as the sum of scores for positive words divided by the total word count.
    """
    if not feedback:
        return 0

    # Parse feedback with Beautiful Soup to remove HTML tags
    soup = BeautifulSoup(feedback, 'html.parser')
    text = soup.get_text()

    # Define an expanded list of positive words with associated scores
    positive_words = {
        "exceptional": 3, "excellent": 3, "skilled": 2, "proactive": 2, "dedicated": 2,
        "innovative": 3, "talented": 3, "creative": 2, "passionate": 2, "motivated": 2,
        "strong": 2, "insightful": 2, "organized": 2, "compassionate": 2, "diligent": 2,
        "gifted": 3, "sustainable": 2, "analytical": 2, "leadership": 3, "effective": 2,
        "efficient": 2, "problem-solver": 3, "productive": 2, "outstanding": 3, "expertise": 2
    }

    # Split the feedback text into words and calculate the total score
    words = text.lower().split()
    total_score = sum(positive_words.get(word, 0) for word in words)

    # Calculate the score as the average score per word (normalize by word count)
    normalized_score = total_score / len(words) if words else 0

    return normalized_score

# Section: Fetch and Display Employer Data
st.subheader("Employer Data")

try:
    # Fetch data from the API
    response = requests.get(API_URL)
    response.raise_for_status()  # Raise an error for bad responses
    employer_data = response.json()

    # Convert JSON response to Pandas DataFrame
    employer_df = pd.DataFrame(employer_data)

    # Define column order for display
    desired_columns = [
        "Director_ID", "Director_Name", "Director_Contact", 
        "Student_ID", "Student_Name", "Student_Major", "Student_Program", 
        "Job_Title", "Industry", "Employer_Feedback", "Employer_Name", "Employer_Contact" 
    ]

    # Check if desired columns exist in the data
    missing_columns = [col for col in desired_columns if col not in employer_df.columns]
    if missing_columns:
        st.error(f"Missing columns in the data: {missing_columns}")
    else:
        # Reorder and display the DataFrame
        employer_df = employer_df[desired_columns]

        if 'Employer_Feedback' in employer_df.columns:
            employer_df['Feedback_Score'] = employer_df['Employer_Feedback'].dropna().apply(calculate_score)

        st.dataframe(employer_df)

        # Basic Insights Section
        st.write('')
        st.write('')
        st.subheader("Insights from Employer Data")

        # Total employers
        total_employers = employer_df['Employer_Name'].nunique()

        # Total job positions
        total_jobs = employer_df['Job_Title'].nunique()

        # Most common industry
        common_industry = (employer_df['Industry'].value_counts().idxmax()
                           if not employer_df['Industry'].isnull().all()
                           else "No data")

        # Employer feedback analysis
        avg_feedback_length = employer_df['Employer_Feedback'].dropna().apply(len).mean()

        # Average feedback score
        avg_feedback_score = employer_df['Feedback_Score'].mean()

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Employers", total_employers)
            st.metric("Most Common Industry", common_industry)

        with col2:
            st.metric("Total Job Positions", total_jobs)
            st.metric("Avg Feedback Length", f"{round(avg_feedback_length, 2)} letters")

        with col3:
            st.metric("Avg Feedback Score", f"{round(avg_feedback_score, 2)}")

        # Add explanation for feedback scoring
        st.write("---")
        st.subheader("Feedback Score Explanation")
        st.write("The **Feedback Score** is calculated by assigning points to positive words found in employer feedback. For example:")
        st.write("- Words like **'excellent'**, **'leadership'**, and **'outstanding'** score higher.")
        st.write("- The final score is normalized by dividing the total score by the number of words in the feedback.")
        st.write("This scoring system helps evaluate the quality and positivity of feedback in a visible and easy way.")

        # Visualization: Major with the Highest Feedback Score
        st.write("---")
        st.subheader("Major Feedback Scores")
        if 'Student_Major' in employer_df.columns and 'Feedback_Score' in employer_df.columns:
            major_scores = employer_df.groupby('Student_Major')['Feedback_Score'].mean().sort_values(ascending=False)
            st.bar_chart(major_scores, horizontal=True)

            # Metric for Major with the Highest Feedback Score
            highest_major = major_scores.idxmax()  # Major with the highest score
            highest_major_score = major_scores.max()  # Highest score
            st.metric(f"Top Major by Feedback Score", highest_major, f"{highest_major_score:.2f}")

        # Visualization: Industry with the Highest Feedback Score
        st.write("---")
        st.subheader("Industry Feedback Scores")
        if 'Industry' in employer_df.columns and 'Feedback_Score' in employer_df.columns:
            industry_scores = employer_df.groupby('Industry')['Feedback_Score'].mean().sort_values(ascending=False)
            st.bar_chart(industry_scores, horizontal=True)

            # Metric for Industry with the Highest Feedback Score
            highest_industry = industry_scores.idxmax()  # Industry with the highest score
            highest_industry_score = industry_scores.max()  # Highest score
            st.metric(f"Top Industry by Feedback Score", highest_industry, f"{highest_industry_score:.2f}")


except requests.exceptions.RequestException as e:
    st.error(f"Error fetching employer data: {e}")