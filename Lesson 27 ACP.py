import random
import string

def generate_password(length=12):
    # Define the characters that can be used in the password
    all_characters = string.ascii_letters + string.punctuation

    # Randomly select characters from the list and join them to form the password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Example: Generate a random password of length 12
password = generate_password(12)
print("Generated Password:", password)
