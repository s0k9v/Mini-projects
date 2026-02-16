import py
import sqlite3

def login(username, password):
    if username == "admin" and password == "password":
        return "Login successful!"
    else:
        return "Login failed. Please check your credentials."

def register(username, password):
    print("Input username and password to register.")
    if username and password:
        return "Registration successful!"
    else:
        return "Registration failed. Please provide valid credentials."
def main():
    while True:
        print("Welcome to the Login System")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        
        choice = input("Please select an option: ")
        
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(login(username, password))
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(register(username, password))
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()