# 🎬 Movie Rental Management System

The "Inchiriere_Filme" project is a Python-based application designed to simulate a movie rental system. It serves as a practical demonstration of key programming concepts, such as modularity, data management, and error handling, while providing a real-world solution to a common problem.


## 🏗️ Architecture Overview

The project follows a layered architecture, ensuring clarity, scalability, and maintainability throughout the development process:

-  📦 Domain Layer: Contains the core data entities, defining the fundamental components of the system:

    -  Client — Represents customers with attributes such as unique IDs, names, and personal details.

    -  Film — Represents movies with relevant information like title, genre, and release year.

    -  Inchiriere — Models the relationship between clients and rented movies, including rental and return dates.


-  💾 Repository Layer: Responsible for handling data storage and retrieval:

      -  Implements CRUD (Create, Read, Update, Delete) operations to manage data.

      -  Uses structured text files for persistence:

            -  clienti.txt — Holds client data.

            -  filme.txt — Stores movie records.

            -  inchirieri.txt — Logs all rental transactions.


-  ⚙️ Service Layer: Implements the business logic of the system:

      -  Manages client and movie registration, as well as rental and return operations.

      -  Includes sorting and filtering functionality to enhance data retrieval.



-  🖥️ Console Interface (UI): Provides an interactive user interface via the command line:

      -  Offers a simple, menu-driven navigation system.

      -  Handles input, output, and error management for a smooth user experience.


-  ✅ Validation Module: Ensures data integrity and prevents invalid entries:

      -  Validates unique IDs, non-empty fields, and correct date formats.

      -  Prevents the entry of incorrect or corrupt data into the system.
