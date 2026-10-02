import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password = generate_password(16)

print("Generated Password:", password)

if len(password) >= 12:
    print("Password strength: Strong 💪")
else:
    print("Password strength: Weak ⚠️")
