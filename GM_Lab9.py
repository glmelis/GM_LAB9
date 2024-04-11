#Gian-Luca Melis
#Decoder added by Katelyn Fry
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
            encoded = encode(password)
            print("Your password has been encoded and stored!\n")
        if option == "2":
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}")
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

# Hi! I'm going to add a decoder function!
def decode:
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit)-3) % 10)
        decoded_password += decoded_digit
    return decoded_password

if __name__ == "__main__":
    main()
