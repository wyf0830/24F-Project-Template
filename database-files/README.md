# `database-files` Folder

TODO: Put some notes here about how this works.  include how to re-bootstrap the db. 

###
Folder Description
This folder contains files and data related to the application database for storing and managing core data such as student information, employer information, feedback, and recommendations.

File Description
1. 00_coopApp.sql.
This file contains the table structure definition (Schema) of the database, including detailed definitions of all tables, fields, indexes and foreign keys.
It is used to initialize the database structure.

2. 01_coopApp_data.sql.
Contains initial test data (Seed Data) used to populate database tables for development and testing.
Data includes sample students, employers, feedback records, and referral entries.

3. database.db.
SQLite database file containing the complete database contents currently being used by the application.
Initialized via 00_coopApp.sql and 01_coopApp_data.sql.

* Usage Instruction
- If you need to restart the database, delete or backup the existing database.db file:
'''
rm database-files/database.db
'''

- Backing up the database: If you have important data, back up the existing database.db file before purging or reinitializing:
'''
cp database-files/database.db database-files/backup_database.db
'''