import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    print("----------------------------------")

    # Get user input for password length
    length = int(input("Enter the desired length of the password: "))

    # Get user input for the number of passwords to generate
    num_passwords = int(input("Enter the number of passwords to generate: "))

    # Generate and display passwords
    print("\nGenerated Passwords:")
    for i in range(num_passwords):
        password = generate_password(length)
        print(password)

if __name__ == "__main__":
    main()
