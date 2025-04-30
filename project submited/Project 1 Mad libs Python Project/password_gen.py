import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password has at least one of each type
    length = 12  # Set the password length to 12 characters
    all_characters = lower + upper + digits + symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
        print("Generated Password:", generate_password(length))
    except ValueError as e:
        print("Error:", e)