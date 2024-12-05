import sqlite3
from faker import Faker
import random
import os

# Debugging: Print current working directory and database path
print("Current Working Directory:", os.getcwd())
print("Database Path:", "/Users/allenyang/Desktop/cs3200 project/database.db")

# Initialize Faker and database connection
fake = Faker()
conn = sqlite3.connect("/Users/allenyang/Desktop/cs3200 project/database.db")
cursor = conn.cursor()

# Check if the Employer table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Employer';")
if not cursor.fetchone():
    print("Error: 'Employer' table does not exist in the database.")
    conn.close()
    exit()

# Generate sample data for the Employer table
industries = ["Software", "Healthcare", "Finance", "Education", "Logistics"]

for _ in range(40):  # Generate 40 rows
    employer_name = fake.company()
    contact_email = fake.email()
    industry_type = random.choice(industries)
    cursor.execute(
        "INSERT INTO Employer (Name, Contact_Info, Industry) VALUES (?, ?, ?)",
        (employer_name, contact_email, industry_type)
    )

# Commit and close
conn.commit()
conn.close()

print("40 rows added to the Employer table.")
