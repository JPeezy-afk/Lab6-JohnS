# John Paul Schneuker Diaz
# Encodes password, shifting up each digit in the password by 3 numbers
def encoder(password):
    encoded_password = ""
    for digit in password:
        digit = int(digit)
        digit += 3
        encoded_password += str(digit % 10)
    return encoded_password

# Main function
def main():
    while True:
        # Print menu
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit")
        option = int(input("Please enter an option: "))
        # If option == 1, encode user-inputted password
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!")
        # If option == 2, decode encoded passwords
        elif option == 2:
            pass
        # Else, exit loop
        else:
            break

if __name__ == "__main__":
    main()