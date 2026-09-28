# Patient-Data-Monitoring-System

## Project Overview

The Patient Data Monitoring System is a beginner-friendly Python application designed to manage basic healthcare records in an organized way. The system provides separate modules for patient management, appointment management, vaccination management, health checks, and report generation.
The project uses Python functions, loops, conditional statements, file handling, string operations, basic calculations, and modular programming. Data is stored using text files, making the system simple and suitable for an academic Python project.

## Problem Statement

Managing patient information, appointments, vaccination records, and health-check information manually can be difficult and time-consuming. There is a need for a simple system that can store, retrieve, update, and summarize basic healthcare records.
This project provides a menu-driven solution for managing these records using Python and text-file storage.

## Objectives

The main objectives of this project are:
* To develop a simple healthcare record-management system using Python.
* To manage patient information efficiently.
* To book, search, view, and cancel appointments.
* To maintain vaccination records.
* To identify vaccinations that are due.
* To store basic health-check information.
* To calculate BMI using height and weight.
* To generate simple healthcare reports.
* To demonstrate modular programming and file handling.

## Features

### Patient Management
* Add patient
* View patients
* Search patient
* Update patient

### Appointment Management
* Book appointment
* View appointments
* Search appointment
* Cancel appointment

### Vaccination Management
* Add vaccination
* View vaccination records
* Search vaccination
* Automatically add a missing vaccination as Due

### Health Check
* Add health-check record
* View health-check records
* Calculate BMI
* Display BMI category

### Reports
* Patient report
* Appointment report
* Vaccination report
* Health report
* Display due vaccinations
* Display BMI information

## Technologies Used

* Programming Language: Python
* Data Storage:Text files (`.txt`)
* Development Approach: Modular programming
* Interface:Command-line / menu-driven interface

## Project Structure

Patient_Data_Monitoring_System/
│
├── main.py
├── patient.py
├── appointment.py
├── vaccination.py
├── health_check.py
├── reports.py
│
├── patients.txt
├── appointments.txt
├── vaccinations.txt
├── health_checks.txt
│
├── README.md
└── statement.md

## Modules

### `main.py`
Acts as the central control module. It displays the main menu and connects all other modules using imports and function calls.

### `patient.py`
Manages patient records and provides functions for adding, viewing, searching, and updating patients.

### `appointment.py`
Manages appointments, including booking, viewing, searching, and cancelling appointments.

### `vaccination.py`
Maintains vaccination records. If a requested vaccine is not found for a patient during a search, the system adds it as a **Due** vaccination.

### `health_check.py`
Stores basic health measurements such as weight, height, blood pressure, and blood sugar. It also calculates BMI.

### `reports.py`
Reads stored records and generates summary reports for patients, appointments, vaccinations, and health checks.

##  Data Files
The system uses four text files for storing data:
patients.txt
appointments.txt
vaccinations.txt
health_checks.txt

The records are stored using the `|` symbol as a separator.

Example:
P001|Rahul|25|Male|9876543210|None|Low

##  How to Run the Project

### Step 1: Install Python
Make sure Python is installed on your computer.

### Step 2: Download or Clone the Repository
Download the project files or clone the GitHub repository.

### Step 3: Open the Project Folder
Open the project folder in an editor such as VS Code, IDLE, or PyCharm.

### Step 4: Run `main.py`
Run:
python main.py
The main menu will appear.

##  Main Menu

The application provides the following menu:
======================================
   PATIENT HEALTH MONITORING SYSTEM
======================================
1. Patient Management
2. Appointment Management
3. Vaccination Management
4. Health Check
5. Reports
6. Exit

The user can select the required module by entering the corresponding number.

## Example

A typical vaccination search works as follows:
Enter Patient ID: P001
Enter Vaccine Name: Polio

If the vaccine is already recorded, the vaccination details are displayed.
If it is not found:

Vaccination not found.
Enter New Vaccination ID: V002
Enter Due Date: 25-10-2026
Vaccination added as Due.

## BMI Calculation

The Health Check module calculates BMI using:
BMI = Weight / (Height in metres × Height in metres)
The system then displays a basic BMI category.
Below 18.5       → Underweight
18.5 – 24.9      → Normal
25 – 29.9        → Overweight
30 or above      → Obesity

The BMI feature is included for educational and demonstration purposes.

## Testing

The project was tested using different valid and invalid inputs for each module.
Testing included:
* Adding and searching patients
* Updating patient information
* Booking and cancelling appointments
* Searching vaccination records
* Adding missing vaccinations as due
* Adding health-check records
* Calculating BMI
* Generating reports
* Testing invalid menu choices

The tested functions produced the expected results for the defined test cases.

## Limitations

The current version has some limitations:
* Data is stored in text files instead of a database.
* There is no user authentication.
* Data is not encrypted.
* Input validation is basic.
* The system does not provide medical diagnosis.
* The application uses a command-line interface.

## Future Enhancements

Future versions could include:
* SQLite or MySQL database integration
* User login and authentication
* Graphical user interface using Tkinter
* Appointment reminders
* Automatic vaccination schedules
* Better input validation
* PDF report generation
* Data backup
* More detailed preventive-care features

## Conclusion

The Patient Health Monitoring & Preventive Care System demonstrates how basic Python programming concepts can be combined to create a practical, modular application. The project provides functionality for managing patients, appointments, vaccinations, health checks, and reports while using text files for data storage. It provides practical experience with functions, loops, conditional statements, file handling, calculations, and modular programming.

## Author
Name: Elaine Mary Thomas
Student ID: 26BHI10101
Course: Introduction to Problem Solving and Programming
Institution: Vellore Institute of Technology, Bhopal
