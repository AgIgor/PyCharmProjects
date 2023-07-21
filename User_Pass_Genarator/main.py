import secrets
import time

token = secrets.token_urlsafe(10)
email = f'{token}@outlook.com'
pwd = secrets.token_urlsafe(10)
data = f'{time.asctime()} {email} {pwd}\n'

with open("teste.txt", "a") as f:
    f.write(data)

print(data)



