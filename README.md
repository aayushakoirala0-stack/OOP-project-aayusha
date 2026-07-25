# Library Management System

## Introduction

The Library Management System is a console-based Python application developed using Object-Oriented Programming (OOP). It is designed to manage books, library members, and book issuing and returning operations.

The system demonstrates important OOP concepts such as abstraction, inheritance, encapsulation, classes, and objects. It also uses JSON file storage to save library data permanently.

## Features

- Add new books
- Display available books
- Search for books
- Register student members
- Register faculty members
- Display registered members
- Issue books to members
- Return books
- Save and load data using JSON
- Handle invalid inputs using exception handling

## OOP Concepts Used

### Abstraction
Abstract Base Classes are implemented using Python's `ABC` and `abstractmethod`.

### Inheritance
Inheritance is used between:
- `LibraryItem` → `Book`
- `Member` → `StudentMember`
- `Member` → `FacultyMember`

### Encapsulation
Private attributes using double underscores are used to protect data inside classes.

Examples:
- `__title`
- `__author`
- `__available`
- `__member_id`
- `__name`

### Exception Handling
`try-except` blocks are used to handle invalid user input and file-related errors.

## Data Persistence

The system stores library information in a JSON file named:

`library_data.json`

This allows book and member information to remain available even after the program is closed.

## Technologies Used

- Python
- Object-Oriented Programming
- JSON
- Visual Studio Code
- GitHub

## Project Files

- `library.py` – Contains the classes and library operations.
- `main.py` – Contains the main menu and user interaction.
- `library_data.json` – Stores library data permanently.
- `README.md` – Provides information about the project.

## How to Run

1. Make sure Python is installed.
2. Open the project folder in Visual Studio Code.
3. Open `main.py`.
4. Run the Python file.
5. Select options from the menu to manage books and members.

## Conclusion

This project demonstrates how Object-Oriented Programming concepts can be applied to develop a simple and organized Library Management System. It also provides practical experience with inheritance, abstraction, encapsulation, exception handling, and JSON data persistence.