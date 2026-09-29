# Hospital Management System

## Overview

The Hospital Management System is a simple Python project made to manage basic hospital activities.

The project allows the user to add and view patient information, search for a patient, and manage basic appointments. It is a console-based application, so it runs directly in the terminal.

This project was created as a beginner-level Python project to practice basic Python programming concepts.

## Features

The system currently provides the following features:

* Add a new patient
* View all patients
* Search for a patient using Patient ID
* Book an appointment
* View appointments
* Exit the application

## Technologies Used

* Python
* VS Code
* Git
* GitHub

## Python Concepts Used

This project uses basic Python concepts such as:

* Variables
* Lists
* `input()` and `print()`
* `if`, `elif`, and `else`
* `while` loop
* `for` loop
* Functions/modules can be added for further expansion
* Basic data management using lists

## Project Structure

```text
Hospital-Management-System/
│
├── main.py
├── patients.py
├── doctors.py
├── appointments.py
├── billing.py
├── file_handler.py
│
├── data/
│   ├── patients.txt
│   ├── doctors.txt
│   └── appointments.txt
│
├── tests/
│   └── test_project.py
│
├── README.md
├── statement.md
└── .gitignore
```

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

You can check it by opening the terminal and running:

```bash
python --version
```

### 2. Clone the Repository

Clone this repository to your computer:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 3. Open the Project Folder

Open the project folder in VS Code.

### 4. Run the Program

Run the main Python file:

```bash
python main.py
```

The Hospital Management System menu will appear in the terminal.

## Example Menu

```text
===== Hospital Management System =====

1. Add Patient
2. Show Patients
3. Find Patient
4. Book Appointment
5. Show Appointments
6. Exit

Choose an option:
```

## Input and Output

### Patient Management

The user can enter:

* Patient ID
* Patient Name
* Age
* Disease

The entered patient information can then be viewed or searched using the Patient ID.

### Appointment Management

The user can enter:

* Patient ID
* Doctor Name
* Date
* Time

The appointment details can then be displayed in the system.

## Testing

The project includes basic testing to check important parts of the program, such as patient information, appointment data, and billing calculations.

Testing helps make sure that the main features work correctly.

## Limitations

This is a beginner-level console application. It currently does not include:

* Graphical User Interface
* Online appointment booking
* Database connectivity
* User login system
* Real hospital data

The project uses simple Python data structures and text files for learning purposes.

## Future Enhancements

The project can be improved in the future by adding:

* Patient update and delete options
* Doctor management
* Billing system
* Login and authentication
* Database support
* Graphical User Interface
* Appointment cancellation
* Better input validation
* Hospital staff management

## Learning Outcomes

Through this project, I practiced:

* Writing Python programs
* Using lists and loops
* Using conditional statements
* Taking input from users
* Organizing a Python project
* Handling basic files
* Using Git and GitHub
* Testing and debugging Python programs

## Author

**Ansh Gujar**

This project was created as part of a Python learning project.
