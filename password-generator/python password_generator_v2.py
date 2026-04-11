import random

continue_choice = "y"

# keeps regenerating if user chooses to generate more than one password

while continue_choice.lower() == "y":

    print("welcome to password generator!")

    # taking password preferences
    use_upper = input("\n\t-> do you want to include uppercase letters? y/n: ")
    use_lower = input("\t-> do you want to include lowercase letters? y/n: ")

    while use_upper.lower() == "n" and use_lower.lower() == "n":
        print("at least 1 alphabet is mandatory.")
        use_upper = input("\n\t-> do you want uppercase? y/n: ")
        use_lower = input("\t-> do you want lowercase? y/n: ")

    use_digits = input("\t-> do you want to include digits? y/n: ")
    use_symbols = input("\t-> do you want to include symbols? y/n: ")

    # converting input to lowercase for further evaluation
    use_upper = use_upper.lower()
    use_lower = use_lower.lower()
    use_digits = use_digits.lower()
    use_symbols = use_symbols.lower()

    # initializing empty string to store allowed characters
    characters = ""

    if use_upper == 'y':
        characters += ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if use_lower == 'y':
        characters += ("abcdefghijklmnopqrstuvwxyz")
    if use_digits == 'y':
        characters += ("1234567890")
    if use_symbols == 'y':
        characters += ("~!@#$%^&*")
    if not characters:
        print("select at least one option to continue.")
        continue

    # taking preferred length of password from user
    while True:
        try:
            length = int(input("\nwhat length of the password would you prefer?: "))
            break
        # handle error if the user types in another data type other than integer
        except ValueError:
            print("length can only be an integer. try again.")

    password = ""
    
    # creating password using random module
    for i in range(length):
        password += random.choice(characters)
    
    print("\nyour password is:", password)

    # checking strength
    lower = 0
    upper = 0
    digits = 0
    symbols = 0

    for i in password:
        if i.isalnum():
            if i.isalpha():
                if i.islower():
                    lower += 1
                elif i.isupper():
                    upper += 1
            elif i.isdigit():
                digits += 1
        elif i in "~!@#$%^&*":
            symbols += 1
    
    # checking strength
    if lower > 0 and upper > 0 and digits > 0 and symbols > 0:
        strength = "extremely strong! :3"
    elif lower > 0 and upper > 0 and (digits > 0 or symbols > 0):
        strength = "medium! :)"
    elif lower > 0 or upper > 0:
         strength = "weak! :/"
    else:
        strength = "very weak :("

    # printing final result
    print("\n--------------------------")
    print("your password:", password)
    print(f"strength: {strength}")
    print("--------------------------")

    # asking user if they want to continue making a password
    continue_choice = input("\n\ndo you want to continue making a pass? y/n: ")
