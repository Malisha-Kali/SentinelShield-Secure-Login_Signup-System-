# Secure-Login_Signup-System (Version 1.0.0)
 This is a Secure Login and Signup sysem Iniatially. In future this will be upgrade to ful Secure Login System.


## Used Technoly for The Registration process Securly Store the passwords of users

The technology used for password protection in the provided code is bcrypt. Bcrypt is a password hashing function designed to securely hash passwords. It incorporates a salt to protect against rainbow table attacks and uses the Blowfish cipher. Here's how it works in the code:

Hashing Passwords: When a user registers, their password is hashed using bcrypt before storing it in the database. This is done using the bcrypt.hashpw() function, which takes the password in plain text and generates a hashed version of it.

Salt: Bcrypt automatically generates and manages a random salt for each password hash. The salt is stored along with the hash, making each hash unique even if two users have the same password.

Verifying Passwords: When a user attempts to log in, their entered password is hashed using bcrypt and compared to the hashed password stored in the database. This comparison is done using the bcrypt.checkpw() function, which takes the entered password and the stored hashed password, returning True if they match and False otherwise.

Bcrypt is a widely used and trusted technology for password hashing due to its security features and resistance to brute-force and rainbow table attacks. It's considered one of the best practices for securely storing passwords in databases.


# Version 1.1.0

including password policy when Regisration

# Version 2.0.0

MFA Added
