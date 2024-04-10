def main():
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")
        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            encode(password)
        if option == "3":
            break
        else:
            continue

def encode:
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

if __name__ == "__main__":
    main()