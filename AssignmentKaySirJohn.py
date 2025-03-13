# 1.) function for determining a number an odd or even
def check_number(number):
    # Check if input is empty
    if len(number) < 1:
        return "Please enter a number."
   
    # Check if input is more than one number
    if not number.isdigit():
        return f"'{number}' is not a valid number."
   
    # Convert to integer and check if odd or even
    num = int(number)
    if num % 2 == 0:
        return f"'{num}' is Even"
    else:
        return f"'{num}' is Odd"


# 2.) function for determining a letter if vowel or consonant
def check_letter(letter):
    vowels = "aeiouAEIOU"
   
    # Check if input is empty
    if len(letter) < 1:
        return "Please enter a character."
   
    # Check if input is more than one character
    if len(letter) > 1:
        return "Please enter a single character only."
   
    # Check if input is a letter
    if letter.isalpha():
        if letter in vowels:
            return f"'{letter}' is Vowel"
        else:
            return f"'{letter}' is Consonant"
    else:
        return f"'{letter}' is not a letter."


# 3.) function for determining a character if it is special character
def check_special(char):
    # List of special characters
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/`~'\""
   
    # Check if input is empty
    if len(char) < 1:
        return "Please enter a character."
   
    # Check if input is more than one character
    if len(char) > 1:
        return "Please enter a single character only."
   
    # Check if input is a special character
    if char in special_chars:
        return f"'{char}' is a Special Character"
    elif char.isalpha():
        return f"'{char}' is a Letter"
    elif char.isdigit():
        return f"'{char}' is a Number"
    else:
        return f"'{char}' is a Space or Other Character"


# 4.) function for analyzing multiple characters
def check_multiple(char):
    # List of special characters and vowels
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/`~'\""
    vowels = "aeiouAEIOU"
   
    # Check character type
    if char in special_chars:
        return f"'{char}' is a Special Character"
    elif char.isalpha():
        if char in vowels:
            return f"'{char}' is a Vowel Letter"
        else:
            return f"'{char}' is a Consonant Letter"
    elif char.isdigit():
        num = int(char)
        if num % 2 == 0:
            return f"'{char}' is an Even Number"
        else:
            return f"'{char}' is an Odd Number"
    elif char.isspace():
        return f"'{char}' is a Space"
    else:
        return f"'{char}' is Other Character"


def display_menu():
    print("\n=== Character Analysis Program ===")
    print("1. Check if number is Odd or Even")
    print("2. Check if letter is Vowel or Consonant")
    print("3. Check if character is Special Character")
    print("4. Analyze multiple characters")
    print("Type 'stop' to exit the program")
    print("================================")


def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ").lower()
       
        # Check for stop command
        if choice == 'stop':
            print("\nThank you for using the program!")
            break
           
        # Process menu choices
        if choice == '1':
            print("\n=== Odd or Even Checker ===")
            user_input = input("Enter a number: ")
            result = check_number(user_input)
            print(result)
               
        elif choice == '2':
            print("\n=== Vowel or Consonant Checker ===")
            user_input = input("Enter a letter: ")
            result = check_letter(user_input)
            print(result)
               
        elif choice == '3':
            print("\n=== Special Character Checker ===")
            user_input = input("Enter a character: ")
            result = check_special(user_input)
            print(result)
               
        elif choice == '4':
            print("\n=== Multiple Character Analyzer ===")
            user_input = input("Enter characters: ")
            if len(user_input) < 1:
                print("Please enter at least one character.")
                continue
            print("\nAnalyzing each character:")
            for character in user_input:
                result = check_multiple(character)
                print(result)
            print()
               
        else:
            print("\nInvalid choice! Please select a number between 1-4 or type 'stop'")


# Start the program
if __name__ == "__main__":
    main()