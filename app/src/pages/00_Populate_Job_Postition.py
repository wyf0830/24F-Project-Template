import sqlite3
from faker import Faker
import random

# Initialize Faker and database connection
fake = Faker()
conn = sqlite3.connect("/Users/allenyang/Desktop/cs3200 project/database.db")
cursor = conn.cursor()

# Fetch all Employer_IDs
cursor.execute("SELECT Employer_ID FROM Employer")
employer_ids = [row[0] for row in cursor.fetchall()]

# Generate sample data for the Job_Position table
for _ in range(50):  # Generate 50 job positions
    employer_id = random.choice(employer_ids)
    title = fake.job()
    requirement = fake.sentence(nb_words=10)
    description = fake.text(max_nb_chars=200)
    cursor.execute(
        "INSERT INTO Job_Position (Employer_ID, Title, Requirement, Description) VALUES (?, ?, ?, ?)",
        (employer_id, title, requirement, description)
    )

# Commit and close
conn.commit()
conn.close()

print("50 rows added to the Job_Position table.")
