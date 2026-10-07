# Early Registration & Messenger Prototype (Eel + MySQL)

An old learning project created when I was first starting out with backend development, trying to connect a web frontend with Python, and learning how to work with relational databases.

## What it does
* **Web-to-Python Bridge:** Uses **Eel** to run a local HTML/JS registration page (`register.html`) and expose Python functions directly to the frontend interface.
* **Database Management:** Connects to a **MySQL** database, automatically creates the `Users` table on startup if it doesn't exist, and checks for duplicates before inserting records.
* **Phone Validation & Normalization:** Includes custom logic to validate incoming phone numbers (checking prefixes like `+7` or `8` and operator codes) and normalizes them down to the last 10 digits before saving.

## Technologies Used
* **Python**
* **Eel** (for desktop web UI development)
* **MySQL** (database connectivity and queries)
* **HTML / JavaScript** (frontend UI)

---
> **Project Status:** Abandoned (Early educational pet project).
---
