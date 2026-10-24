🔐 Secure Login System

A simple command-line Secure Login System built with Python.
The project demonstrates user registration, secure password hashing, password verification, and login authentication.

📌 Features

- 👤 User registration
- 🔑 Password-based login
- 🔒 Password hashing using PBKDF2-HMAC-SHA256
- 🧂 Random 16-byte salt for each password
- 🛡️ Secure password comparison using "hmac.compare_digest()"
- 🚫 Minimum password length of 8 characters
- 💻 Simple command-line interface

🛠️ Technologies Used

- Python 3
- "hashlib"
- "hmac"
- "getpass"
- "os"

These modules are part of Python's standard library, so no external packages are required.

📂 Project Structure

secure-login-system/
│
├── secure_app.py
└── README.md

🚀 Getting Started

1. Clone the repository

git clone https://github.com/your-username/secure-login-system.git

2. Navigate to the project directory

cd secure-login-system

3. Run the application

python secure_app.py

💻 How It Works

Registration

The user enters a username and password. The application checks that the username is not empty and that the password contains at least 8 characters.

A random salt is generated and the password is processed using PBKDF2 with SHA-256 and 100,000 iterations. Only the salt and password hash are stored in the in-memory user dictionary.

Login

During login, the entered username is searched in the stored users. The password is then hashed using the stored salt and compared with the stored password hash using "hmac.compare_digest()".

🖥️ Example

==================================================
          SECURE LOGIN SYSTEM
==================================================

1. Register
2. Login
3. Exit

Choose option: 1

Create username: alice
Create password:
User registered successfully.

Then:

1. Register
2. Login
3. Exit

Choose option: 2

Username: alice
Password:
Login successful.

🔐 Security Concepts Demonstrated

This project demonstrates several important authentication concepts:

- Password hashing instead of storing passwords directly
- Salting to make password hashes harder to attack
- PBKDF2 to make password cracking more computationally expensive
- Constant-time comparison using "hmac.compare_digest()"
- Hidden password input using Python's "getpass" module

⚠️ Limitations

This is an educational project and is not intended for production authentication systems.

Currently:

- User data is stored only in memory.
- All registered users are lost when the program exits.
- There is no database.
- There is no password reset functionality.
- There is no account lockout or rate limiting.
- There is no email verification.
- The application is command-line based.

🔮 Future Improvements

Possible improvements include:

- Add SQLite/MySQL database support
- Store users persistently
- Add password reset functionality
- Add account lockout after multiple failed attempts
- Add username validation
- Add password-strength checking
- Add logging and audit records
- Build a web interface
- Add multi-factor authentication (MFA)

📚 Learning Objectives

This project is useful for learning:

- Python functions
- User input handling
- Password authentication
- Cryptographic hashing
- Salting
- Secure password verification
- Basic cybersecurity concepts

👩‍💻 Author

Your Name

GitHub: "https://github.com/your-username"

---

⭐ If you found this project useful, consider giving the repository a star!
