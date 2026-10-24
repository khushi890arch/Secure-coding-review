import os
import hashlib
import hmac
import getpass


users = {}


def hash_password(password, salt=None):

    if salt is None:
        salt = os.urandom(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )

    return salt, password_hash


def verify_password(password, salt, stored_hash):

    _, password_hash = hash_password(password, salt)

    return hmac.compare_digest(
        password_hash,
        stored_hash
    )


def register():

    username = input("Create username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    password = getpass.getpass("Create password: ")

    if len(password) < 8:
        print("Password must contain at least 8 characters.")
        return

    salt, password_hash = hash_password(password)

    users[username] = {
        "salt": salt,
        "password_hash": password_hash
    }

    print("User registered successfully.")


def login():

    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")

    user = users.get(username)

    if user is None:
        print("Invalid username or password.")
        return

    if verify_password(
        password,
        user["salt"],
        user["password_hash"]
    ):
        print("Login successful.")
    else:
        print("Invalid username or password.")


print("=" * 50)
print("          SECURE LOGIN SYSTEM")
print("=" * 50)

while True:

    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid option.")