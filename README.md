# Fall 2024 CS 3200 Project: Cooperative Education Management System

This repository contains the semester project for managing and analyzing cooperative education data. The project includes a web-based platform with features for managing students, advisors, employers, and program performance metrics. It showcases a complete application stack with a database, REST API, and front-end web application.

Youtube video link: https://youtu.be/cbNH7vSN8hw

## Prerequisites

- A GitHub Account
- A terminal-based or GUI Git client
- Visual Studio Code (VSCode) with the Python Plugin
- Python installed on your machine (via `brew`, `choco`, or a Python distribution like Anaconda)
- Docker installed and running

## Current Project Components

This project is composed of three primary components, each running in its own Docker container:

- **Streamlit App** (`./app` directory): Front-end for visualizing and managing the system data.
- **Flask REST API** (`./api` directory): Back-end for handling requests and providing data to the app.
- **SQL Database** (`./database-files` directory): SQL files for database schema and seed data.

---

## Key Features of the Project

1. **Student Management**:
   - Add, update, and delete student information.
   - View and analyze student data, including their majors and program status.

2. **Advisor Tools**:
   - Manage student-advisor relationships.
   - Provide recommendations for cooperative education programs.

3. **Employer Partnership Management**:
   - Track employer feedback and job positions.
   - Analyze industry trends and feedback scores.

4. **Program Metrics**:
   - View and manage performance reports for cooperative education programs.
   - Generate insights on placement rates, employer feedback, and program growth.

5. **Admin Dashboard**:
   - Monitor system logs, reports, and backup schedules.
   - Add, update, or delete admin-related data.

6. **Role-Based Access Control (RBAC)**:
   - Users are assigned roles (e.g., Program Director, Administrator, Advisor) to access role-specific features and pages.

---

### Personal Repository Setup

1. Fork this repository to your GitHub account.
2. Clone your forked repository to your local machine:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git


## Controlling the Containers

- `docker compose up -d` to start all the containers in the background
- `docker compose down` to shutdown and delete the containers
- `docker compose up db -d` only start the database container (replace db with the other services as needed)
- `docker compose stop` to "turn off" the containers but not delete them. 

