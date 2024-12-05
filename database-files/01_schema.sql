DROP TABLE IF EXISTS Employer;
DROP TABLE IF EXISTS Job_Position;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Coop_Application;

CREATE TABLE Employer (
    Employer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Contact_Info TEXT NOT NULL UNIQUE,
    Industry TEXT NOT NULL
);

CREATE TABLE Job_Position (
    Position_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Employer_ID INTEGER NOT NULL,
    Title TEXT NOT NULL,
    Requirement TEXT NOT NULL,
    Description TEXT,
    FOREIGN KEY (Employer_ID) REFERENCES Employer (Employer_ID)
);

CREATE TABLE Student (
    Student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Major TEXT NOT NULL,
    Interests TEXT,
    Profile_Status TEXT NOT NULL
);

CREATE TABLE Coop_Application (
    Application_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Student_ID INTEGER NOT NULL,
    Position_ID INTEGER NOT NULL,
    Employer_ID INTEGER NOT NULL,
    Status TEXT NOT NULL,
    Submission_Date DATE NOT NULL,
    FOREIGN KEY (Student_ID) REFERENCES Student (Student_ID),
    FOREIGN KEY (Position_ID) REFERENCES Job_Position (Position_ID),
    FOREIGN KEY (Employer_ID) REFERENCES Employer (Employer_ID)
);
