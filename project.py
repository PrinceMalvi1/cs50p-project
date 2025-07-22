import pyfiglet
import json

def main():
    print("🚀RUNNING EXPENSE TRACKER")
    username = input("What is your name: ")
    print(welcome_user(username))

    while True:
        print("~Expense Tracker~")
        

def



def welcome_user(username):

    banner = pyfiglet.figlet_format(f"Welcome {username}!")
    return banner

if __name__ == "__main__":
    main()




