# `pages` Folder
This folder contains all the pages that make up the application's user interface. Each page is designed to fulfill specific functionality and cater to the requirements of different roles or personas within the application. Detailed documentation on the number of required pages and their structure will be provided in the Phase 3 documentation.

These pages demonstrate the features of the Streamlit framework while enforcing functionality limitations based on roles and personas (e.g., administrators, advisors, and general users). They illustrate how specific components can be used in conjunction with backend integrations but are not intended to represent a fully developed application.

Structure and Features

Role-Based Pages:
Each page is designed to align with the specific requirements of roles or personas. Examples include:
Advisors: Pages such as "Feedback Tracking" and "Schedule Management."
Administrators: Pages such as "Data Reporting" and "Resource Management."

Interactivity:
Pages include interactive elements like buttons, forms, and data visualizations.
Backend integration ensures data is dynamically fetched or updated based on user inputs.
Dynamic visualizations (e.g., bar charts, heatmaps, and scatter plots) are incorporated for data representation.

Database Integration:
Pages interact with the backend database using secure API endpoints or SQL queries.
Database operations include retrieving, updating, and deleting data triggered by user actions.

Page Ordering:
Pages are logically ordered to provide smooth navigation.
Examples: "Home" and "Dashboard" are primary landing pages, while "Settings" or "Reports" act as auxiliary tools.

Security:
Database operations should have basic privilege control to prevent unauthorized users from accessing or modifying data.
The use of parameterized queries to prevent SQL injection and other security risks.

