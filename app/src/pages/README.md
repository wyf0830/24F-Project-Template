# `pages` Folder

This folder contains all the pages that will be part of the application. Details on required numbers will be provided in the Phase 3 documentation.

These pages are meant to show you an example of some of the features of Streamlit and the way we will limit functionality access by role/persona. It is not meant to represent a complete application.

TODO: Describe the pages folder and include link to documentation. Don't forget about ordering of pages.


The "pages" folder contains pages in the application, each of which is directly associated with certain key (button) functions in the website's user interface (UI). These buttons interact with the database in the backend of the application through page logic to store, query, update, or delete data.

Function Overview
* Keystroke Function Description:
1. The keys (buttons) in the page are designed to directly correspond to specific database operations, for example:
2. Data Query: Get relevant information from the database and display it on the page.
3. Data Entry: User fills out the form on the page and saves the new data to the database.
4. Data Update: User modifies the content on the page and updates it to the database.
5. Data Deletion: Remove the specified data from the database by key operation.
* Database interaction logic:
Each page contains back-end logic to interact with the database, using appropriate APIs or database drivers (e.g., SQLAlchemy, PyMySQL) to accomplish data operations.

Page Design Principles
1. Functional clarity:
Each page corresponds to a specific database table or functional module to ensure that the page function is consistent with the database structure.
The mapping relationship between page keys and database operations should be clearly commented in the code.

2. Security:
Database operations should have basic privilege control to prevent unauthorized users from accessing or modifying data.
The use of parameterized queries to prevent SQL injection and other security risks.
Interactivity:


