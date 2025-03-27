# 🎬 Movie Rental Management System

The *"Inchiriere_Filme"* project is a Python-based application designed to simulate a movie rental system. It serves as a practical demonstration of key programming concepts, such as modularity, data management, and error handling.


## 🏗️ Architecture Overview

The project follows a layered architecture, ensuring clarity, scalability, and maintainability throughout the development process:

-  📦 **Domain Layer**: Contains the core data entities, defining the fundamental components of the system:

    -  Client — Represents customers with attributes such as unique IDs, names, and personal details.

    -  Film — Represents movies with relevant information like title, genre, and release year.

    -  Inchiriere — Models the relationship between clients and rented movies, including rental and return dates.


-  💾 **Repository Layer**: Responsible for handling data storage and retrieval:

      -  Implements CRUD (Create, Read, Update, Delete) operations to manage data.

      -  Uses structured text files for persistence:

            -  clienti.txt — Holds client data.

            -  filme.txt — Stores movie records.

            -  inchirieri.txt — Logs all rental transactions.


-  ⚙️ **Service Layer**: Implements the business logic of the system:

      -  Manages client and movie registration, as well as rental and return operations.

      -  Includes sorting and filtering functionality to enhance data retrieval.



-  🖥️ **Console Interface (UI)**: Provides an interactive user interface via the command line:

      -  Offers a simple, menu-driven navigation system.

      -  Handles input, output, and error management for a smooth user experience.



-  ✅ **Validation Module**: Ensures data integrity and prevents invalid entries:

      -  Validates unique IDs, non-empty fields, and correct date formats.

      -  Prevents the entry of incorrect or corrupt data into the system.


## 🗂️ Data Persistence

The system employs a file-based data storage approach, which is easy to implement and maintain:

-  clienti.txt — Stores client information.

-  filme.txt — Contains movie records.

-  inchirieri.txt — Logs rental transactions.

This approach provides simplicity and portability, making it ideal for early-stage software development projects.


## 🌟 Key Features

-  🎯 **Modular Design**: The layered architecture ensures clear separation of concerns, enhancing both code readability and maintainability.

-  🔍 **Input Validation**: Strong validation rules ensure the integrity and consistency of user data, preventing errors and inconsistencies.

-  📤 **Full CRUD Functionality**: The system supports full lifecycle management for clients, movies, and rentals, offering a complete solution for rental transactions.

-  📑 **Sorting & Filtering**: Advanced query options allow users to filter and sort data, improving efficiency in finding specific information.

-  🛠️ **Robust Error Handling**: The system gracefully handles errors, ensuring stability even when faced with invalid inputs or unexpected scenarios.


## 🔬 Technical Highlights
-  **Language**: Python

-  **Architecture**: Multi-layered architecture (Domain, Repository, Service, UI)

-  **Data Persistence**: File-based system using structured text files for storing records

-  **Error Management**: Comprehensive validation and exception handling

The *"Inchiriere_Filme"* project demonstrates practical problem-solving and the application of fundamental software development principles. This project serves as a strong foundation for further work in Python development and systems programming.

