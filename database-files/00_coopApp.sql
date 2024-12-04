DROP DATABASE IF EXISTS `coop_app`;
CREATE DATABASE IF NOT EXISTS `coop_app`;
USE coop_app;


CREATE TABLE IF NOT EXISTS `Employer` (
  `Employer_ID` INTEGER AUTO_INCREMENT NOT NULL,
  `Name` VARCHAR(100) NOT NULL,
  `Contact_Info` VARCHAR(50) NOT NULL,
  `Industry` VARCHAR(50),
  `Profile_Status` TINYINT(1) DEFAULT 1 NOT NULL,
   CONSTRAINT `PK_Employer` PRIMARY KEY (`Employer_ID`)
);


CREATE TABLE IF NOT EXISTS `Job_Position` (
  `Position_ID` INTEGER AUTO_INCREMENT NOT NULL,
  `Employer_ID` INT NOT NULL,
  `Title` VARCHAR(100) NOT NULL,
  `Requirement` TEXT NOT NULL,
  `Description` TEXT,
   CONSTRAINT `PK_Job_Position` PRIMARY KEY (`Position_ID`),
   CONSTRAINT `FK_Job_Position` FOREIGN KEY (`Employer_ID`)
       REFERENCES Employer (`Employer_ID`)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


CREATE TABLE IF NOT EXISTS `Student` (
  `Student_ID` INTEGER AUTO_INCREMENT NOT NULL,
  `Name` VARCHAR(100) NOT NULL,
  `Major` VARCHAR(50),
  `Interests` TEXT,
  `Program` VARCHAR(255),
  `Profile_Status` TINYINT(1) DEFAULT 1 NOT NULL,
   CONSTRAINT `PK_Student` PRIMARY KEY (`Student_ID`)
);


CREATE TABLE IF NOT EXISTS `Coop_Application` (
  `Application_ID` INTEGER AUTO_INCREMENT NOT NULL,
  `Student_ID` INT NOT NULL,
  `Position_ID` INT NOT NULL,
  `Employer_ID` INT NOT NULL,
  `Status` TINYINT(1) DEFAULT 1 NOT NULL,
  `Submission_Date` DATE,
   CONSTRAINT `PK_Coop_Application` PRIMARY KEY (`Application_ID`),
   CONSTRAINT `FK_Coop_Application_1` FOREIGN KEY (`Student_ID`)
       REFERENCES Student (`Student_ID`)
       ON UPDATE CASCADE
       ON DELETE RESTRICT,
   CONSTRAINT `FK_Coop_Application_2` FOREIGN KEY (`Position_ID`)
       REFERENCES Job_Position (`Position_ID`)
       ON UPDATE CASCADE
       ON DELETE RESTRICT,
   CONSTRAINT `FK_Coop_Application_3` FOREIGN KEY (`Employer_ID`)
       REFERENCES Employer (`Employer_ID`)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


CREATE TABLE IF NOT EXISTS `Career_Advisor` (
  `Advisor_ID` INTEGER AUTO_INCREMENT NOT NULL,
  `Name` VARCHAR(100) NOT NULL,
  `Contact_Info` VARCHAR(50) NOT NULL,
   `Student_ID` INT NOT NULL,
   CONSTRAINT `PK_Career_Advisor` PRIMARY KEY (`Advisor_ID`),
   CONSTRAINT `FK_Career_Advisor` FOREIGN KEY (`Student_ID`)
       REFERENCES Student (`Student_ID`)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


CREATE TABLE IF NOT EXISTS `Recommendation` (
  `Recommendation_ID` INTEGER AUTO_INCREMENT NOT NULL,
  `Student_ID` INT NOT NULL,
  `Position_ID` INT NOT NULL,
  `Advisor_ID` INT NOT NULL,
  `Content` TEXT,
   CONSTRAINT `PK_Recommendation` PRIMARY KEY (`Recommendation_ID`),
   CONSTRAINT `FK_Recommendation_1` FOREIGN KEY (`Student_ID`)
       REFERENCES Student (`Student_ID`)
       ON UPDATE CASCADE
       ON DELETE RESTRICT,
   CONSTRAINT `FK_Recommendation_2` FOREIGN KEY (`Position_ID`)
       REFERENCES Job_Position (`Position_ID`)
       ON UPDATE CASCADE
       ON DELETE RESTRICT,
   CONSTRAINT `FK_Recommendation_3` FOREIGN KEY (`Advisor_ID`)
       REFERENCES Career_Advisor (`Advisor_ID`)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


CREATE TABLE IF NOT EXISTS `Admin` (
  `Admin_ID` INTEGER AUTO_INCREMENT NOT NULL,
  `Name` VARCHAR(100) NOT NULL,
  `Contact_Info` VARCHAR(50) NOT NULL,
   CONSTRAINT `PK_Admin` PRIMARY KEY (`Admin_ID`)
);


CREATE TABLE IF NOT EXISTS `Backup_Schedule` (
  `Schedule_ID` INTEGER AUTO_INCREMENT NOT NULL,
  `Admin_ID` INT NOT NULL,
  `Frequency` VARCHAR(50) NOT NULL,
  `Last_Backup_Date` DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
   CONSTRAINT `PK_Backup_Schedule` PRIMARY KEY (`Schedule_ID`),
   CONSTRAINT `FK_Backup_Schedule` FOREIGN KEY (`Admin_ID`)
       REFERENCES Admin (`Admin_ID`)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


CREATE TABLE IF NOT EXISTS `System_Logs` (
  `Log_ID` INTEGER AUTO_INCREMENT NOT NULL,
  `Admin_ID` INT NOT NULL,
  `Event_Type` VARCHAR(50),
  `Message` TEXT,
  `Time_Stamp` DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
   CONSTRAINT `PK_System_Logs` PRIMARY KEY (`Log_ID`),
   CONSTRAINT `FK_System_Logs` FOREIGN KEY (`Admin_ID`)
       REFERENCES Admin (`Admin_ID`)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


CREATE TABLE IF NOT EXISTS `Reports` (
  `Report_ID` INTEGER AUTO_INCREMENT NOT NULL,
  `Admin_ID` INT NOT NULL,
  `Generated_Date` DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
  `Content` TEXT,
  `Report_Type` VARCHAR(50),
   CONSTRAINT `PK_Reports` PRIMARY KEY (`Report_ID`),
   CONSTRAINT `FK_Reports` FOREIGN KEY (`Admin_ID`)
       REFERENCES Admin (`Admin_ID`)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


CREATE TABLE IF NOT EXISTS `Program_Director` (
  `Director_ID` INTEGER AUTO_INCREMENT NOT NULL,
  `Name` VARCHAR(100) NOT NULL,
  `Contact_Info` VARCHAR(100) NOT NULL,
   CONSTRAINT `PK_Program_Director` PRIMARY KEY (`Director_ID`)
);


CREATE TABLE IF NOT EXISTS `Program_Metrics` (
  `Metrics_ID` INTEGER AUTO_INCREMENT NOT NULL,
  `Director_ID` INT NOT NULL,
  `Metrics_Name` VARCHAR(100),
   CONSTRAINT `PK_Program_Metrics` PRIMARY KEY (`Metrics_ID`),
   CONSTRAINT `FK_Program_Metrics` FOREIGN KEY (`Director_ID`)
       REFERENCES Program_Director (`Director_ID`)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


CREATE TABLE IF NOT EXISTS `Performance_Report` (
  `Report_ID` INTEGER AUTO_INCREMENT NOT NULL,
  `Director_ID` INT NOT NULL,
  `Summary` TEXT,
  `Date` DATE,
   CONSTRAINT `PK_Performance_Report` PRIMARY KEY (`Report_ID`),
   CONSTRAINT `FK_Performance_Report` FOREIGN KEY (`Director_ID`)
       REFERENCES Program_Director (`Director_ID`)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


CREATE TABLE IF NOT EXISTS `Resource_Allocation` (
  `Allocation_ID` INTEGER AUTO_INCREMENT NOT NULL,
  `Director_ID` INT NOT NULL,
  `Resource_Type` VARCHAR(50),
   CONSTRAINT `PK_Resource_Allocation` PRIMARY KEY (`Allocation_ID`),
   CONSTRAINT `FK_Resource_Allocation` FOREIGN KEY (`Director_ID`)
       REFERENCES Program_Director (`Director_ID`)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);


CREATE TABLE IF NOT EXISTS `Employer_Feedback` (
  `Feedback_ID` INTEGER AUTO_INCREMENT NOT NULL,
  `Metrics_ID` INT NOT NULL,
  `Student_ID` INT NOT NULL,
  `Position_ID` INT NOT NULL ,
  `Details` TEXT,
   CONSTRAINT `PK_Employer_Feedback` PRIMARY KEY (`Feedback_ID`),
   CONSTRAINT `FK_Employer_Feedback1` FOREIGN KEY (`Metrics_ID`)
       REFERENCES Program_Metrics (`Metrics_ID`)
       ON UPDATE CASCADE
       ON DELETE RESTRICT,
   CONSTRAINT `FK_Employer_Feedback2` FOREIGN KEY (`Student_ID`)
       REFERENCES Student (`Student_ID`)
       ON UPDATE CASCADE
       ON DELETE RESTRICT,
   CONSTRAINT `FK_Employer_Feedback3` FOREIGN KEY (`Position_ID`)
       REFERENCES Job_Position (`Position_ID`)
       ON UPDATE CASCADE
       ON DELETE RESTRICT
);
