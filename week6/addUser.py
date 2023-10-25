import os
import subprocess

# print(dir(os))
def new_user():
    confirm = "n"
    while confirm != "y":
        username = input("Enter a username: ")
        print("Use the username '" + username + "'? (y/n)")
        confirm = input().upper()
    os.system("sudo useradd " + username)

new_user()