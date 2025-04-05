
## 🛡️ Salt and Hashing : Secure User Authentication System 

**Salt and Hashing** is a secure user authentication system designed to register and log in users by hashing and salting their passwords. The system utilizes **SQLite** for local data storage and **Bcrypt** for password hashing, ensuring that user credentials are securely handled.

## ✨ Features

This project includes key features such as **user registration**, where passwords are hashed and salted using the **Bcrypt** algorithm before storage, providing enhanced security. **User login** is implemented by comparing the entered password with the stored hash to validate the credentials. Additionally, password masking is supported using the `msvcrt` module (Windows only), ensuring that passwords are not displayed when entered. The system uses **SQLite** for data storage, creating a simple and efficient database for managing user credentials.

##  Getting Started

### Requirements

To run the project, ensure you have **Python 3.x** installed. You will also need to install the following package's is not available, which can be done using the following command:

```bash
pip install bcrypt
pip install msvcrt
pip install sqlite3
```



## How It Works

1.  **Database Setup**: The SQLite database stores usernames and hashed passwords.
    
2.  **Registration**: Passwords are hashed with **Bcrypt** before saving.
    
3.  **Login**: The system compares the entered password (hashed) with the stored one to authenticate the user.



## Example Interaction

1. **Registration** :
``` python 
Select an option:
1. Register a new user
2. Login to your account
3. Exit the system
Enter your choice : 1
Enter a new username : Roy
Enter a new password : ******  (pass = secret)
User registered successfully !!!
Registration successful!
```
---
2.  **Login** :
``` python 
Select an option:
1. Register a new user
2. Login to your account
3. Exit the system
Enter your choice : 2
Enter your username : Roy
Enter your password : ****** (pass  = secret)
Welcome Back, Roy !!!
Login successful!
```
---
3.  **Exiting Program** :
``` python 
Select an option:
1. Register a new user
2. Login to your account
3. Exit the system
Enter your choice : 3
Exiting system...
```
---
→ When user  registered from program the data stores in ``usersdata.db`` file which is data base file . So we can open this file by using **DB Browser (SQLite)** and we see following output by opening database file in it , then

- Open browse data
- in that select users option from dropdown menu

→ And we get this following output.

4.  **usersdata.db** : 
``` plain text
id  username    password_hash
1	Roy	      $2b$12$z5nigDIhMVfWvMW4JniA8.WNK3xs2uf9lBe/M0GB4.qUoTmN.vO06

```

---

## 🤝 Contributing :

If u have any idea's feel free to contribute   
Fork the repository if needed , make your changes, and submit a pull request.

---

## 📜 License :

This project is licensed under the **Apache 2.0 License**.
