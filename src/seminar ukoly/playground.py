FILE_NAME = "playgroundlogin.txt"
import os

def register(email, password):
    with open(FILE_NAME, "a") as file:
        file.write("")
        file.write(f"{email}, {password}\n")
    print("registration succesful!")

def login(email, password):
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                stored_password, stored_email = line.strip().split(',')
                if email == stored_email and password == stored_password:
                    return True
                else:
                    return False
    except FileNotFoundError:
        return False
    
def main():
    print("Welcome to our site!")
    while True:
        choice = input("Would you like to register(r), login(l) or quit(q)? : ")
        if choice == "r":
            print("Please register...")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            register(email, password)
        elif choice == "l":
            print("Please login...")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if login(email, password):
                print("Login succesful!")
            else:
                print("Login not succesful!")
        elif choice == "q":
            break
        else:
            print("Invalid option, try again...")

if __name__ == "__main__":
    os.system("cls")

main()

    




