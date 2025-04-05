# WRITTEN BY OM [byt-ctrl]
# SIMPLE USER AUTHENTICATION SYSTEM USING SQLITE AND BCRYPT

import bcrypt
import msvcrt
import sqlite3
from getpass import getpass

# Setting Up The database creates the users table if its doesn't already exist
def initialize_database():
    # connect to the SQLite database (it will create a file if it doesnot exit)

    conn=sqlite3.connect('usersdata.db')
    c=conn.cursor()

    # create a tablle for storing users data (username and hased password)

    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password_hash TEXT NOT NULL)''')
    
    conn.commit()# commit changes to the database
    conn.close()# close the connection to database

# User Registration -->  Hashes and salts the password before storing 

def register_user(username,password):
    # connecting to sqlite database
    conn=sqlite3.connect('usersdata.db')
    c=conn.cursor()

    # check if the username already exits in the database
    c.execute("SELECT * FROM users WHERE username = ?",(username,))
    user=c.fetchone()

    if user:
        print(" Username already exits. Please choose a diffrent one.")
        return False
    # it returns false if the username already exists .

    # generate a salt and hash the password using bcrypt
    salt=bcrypt.gensalt()
    password_hash=bcrypt.hashpw(password.encode('utf-8'),salt)

    # insert the new user and hashed password into data-base 
    c.execute("INSERT INTO users (username,password_hash) VALUES (?, ?)",(username,password_hash))
    conn.commit()
    conn.close

    print("User registered successfully !!!")
    return True # it returns true if the registration is successfull


# User Login --> Compares the entered password with the stored hash

def login_user(username,password):

    # now cpnnecting to the sqlite database
    conn=sqlite3.connect('usersdata.db')
    c=conn.cursor()

    # fetch the stored password hash for the entered username
    c.execute("SELECT password_hash FROM users WHERE username = ?",(username,))
    user=c.fetchone()

    if user:
        stored_password_hash = user[0]

        # compare the entered password with the stored hashed password
        if bcrypt.checkpw(password.encode('utf-8'),stored_password_hash):
            print(f"Welcome Back, {username} !!!")
            return True
        else:
            print("Incorrect password . Please try again.")
            return False
    else:
        print("Username not found. Please check your username or register.")
        return False
    
# custom password input with masking '*' using msvcrt (support in windows only)

def masked_getpass(promt="Password :"):
    print(promt,end='',flush=True)
    password=""

    while True:
        ch=msvcrt.getch() # read a single chr from keyboard

        if ch==b'\r': # enter key (carriage return)
            print()  # moving to next line
            break

        elif ch==b'\x08': # backspace key
            if password:
                password=password[:-1] # remove last chr from password
                print('\b \b',end='',flush=True) # move cursor back and overwrite with space
        else:
            password+=ch.decode('utf-8') # add the enterred chr to the password
            print('*', end='', flush=True)  # Display '*' for each character entered
    return password  # Return the entered password





# Main function to manage user registration and login flow
def main():
    # Initialize the database and create the users table if necessary
    initialize_database()
    
    while True:
        print("\nSelect an option:")
        print("1. Register a new user")
        print("2. Login to your account")
        print("3. Exit the system")
        
        # Get user input to choose an option
        choice = input("Enter your choice : ")
        
        if choice=='1':  # Register a new user
            username = input("Enter a new username : ")
            password = masked_getpass("Enter a new password : ")
            if register_user(username, password):
                print("Registration successful!")
        
        elif choice=='2':  # User login
            username = input("Enter your username : ")
            password = masked_getpass("Enter your password : ")
            if login_user(username,password) :
                print("Login successful!")
        
        elif choice=='3':  # Exit the system
            print("Exiting system...")
            break  # Exit the program
        
        else:
            print("Invalid choice. Please try again.")  # Invalid option handling

main()
