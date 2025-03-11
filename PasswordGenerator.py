import random
import string

def generate_password():
    print("Password Generator")

    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return

        characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    generate_password()
