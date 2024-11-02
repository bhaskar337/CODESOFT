import string
import random
def genrate_password(length=14):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for i in range(length))
    return password
print(genrate_password())