import random
import string

# User Input: ask for password length
length = int(input("Enter the desired length of the password: "))

# Characters to use: letters, digits, and special symbols
characters = string.ascii_letters + string.digits + string.punctuation

# Generate Password: randomly choose characters
password = ''.join(random.choice(characters) for i in range(length))

# Display the Password
print("Generated Password:", password)
