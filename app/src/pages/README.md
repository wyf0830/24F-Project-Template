# `pages` Folder
This folder contains all the pages that make up the application's user interface. Each page is designed to fulfill specific functionality and cater to the requirements of different roles or personas within the application. Detailed documentation on the number of required pages and their structure will be provided in the Phase 3 documentation.

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

* Keystroke Function Description:
1. The keys (buttons) in the page are designed to directly correspond to specific database operations, for example:
2. Data Query: Get relevant information from the database and display it on the page.
3. Data Entry: User fills out the form on the page and saves the new data to the database.
4. Data Update: User modifies the content on the page and updates it to the database.
5. Data Deletion: Remove the specified data from the database by key operation.

* Database interaction logic:
Each page contains back-end logic to interact with the database, using appropriate APIs or database drivers (e.g., SQLAlchemy, PyMySQL) to accomplish data operations.

1. Functional clarity:
Each page corresponds to a specific database table or functional module to ensure that the page function is consistent with the database structure.
The mapping relationship between page keys and database operations should be clearly commented in the code.

2. Security:
Database operations should have basic privilege control to prevent unauthorized users from accessing or modifying data.
The use of parameterized queries to prevent SQL injection and other security risks.


