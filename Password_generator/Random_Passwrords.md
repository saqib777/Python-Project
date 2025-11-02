"""
Random Password Generator
----------------------------------
This program generates a strong random password
based on user preferences for length and character types.

Concepts covered:
- Using Python's 'random' and 'string' modules
- Loops, conditionals, and user input handling
- Building and joining strings dynamically
"""

# Importing the required modules
import random   # For generating random selections
import string   # For accessing predefined character sets (letters, digits, symbols)


def generate_password(length, use_uppercase, use_digits, use_symbols):
    """
    Generates a random password based on user choices.
    
    Parameters:
        length (int): Desired password length
        use_uppercase (bool): Include uppercase letters if True
        use_digits (bool): Include numbers if True
        use_symbols (bool): Include punctuation/symbols if True
    
    Returns:
        str: The generated password
    """
    
    # Start with lowercase letters by default
    characters = list(string.ascii_lowercase)

    # Add more character sets based on user's choices
    if use_uppercase:
        characters += list(string.ascii_uppercase)

    if use_digits:
        characters += list(string.digits)

    if use_symbols:
        characters += list(string.punctuation)

    # If somehow no characters are chosen, return an error
    if not characters:
        return "Error: No character types selected!"

    # Randomly choose characters to form the password
    password = "".join(random.choice(characters) for _ in range(length))

    return password


def main():
    """Main function that interacts with the user and prints the generated password."""
    print("🔐 Welcome to the Random Password Generator!")
    print("You can customize your password strength and length.\n")

    # Get the desired password length
    try:
        length = int(input("Enter desired password length (e.g. 8, 12, 16): "))
        if length <= 0:
            print("⚠️ Length must be greater than zero.")
            return
    except ValueError:
        print("⚠️ Please enter a valid number.")
        return

    # Ask for user preferences
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_symbols = input("Include special symbols? (y/n): ").lower() == "y"

    # Generate the password
    password = generate_password(length, use_uppercase, use_digits, use_symbols)

    # Display the result
    print("\n✅ Your generated password is:")
    print(password)
    print("\n💡 Tip: Store it securely and don't reuse passwords across sites.")


# Entry point check
if __name__ == "__main__":
    main()
