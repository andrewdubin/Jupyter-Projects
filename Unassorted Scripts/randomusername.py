import string
import random

chars = string.ascii_letters + string.digits

smurf = ""

for i in range(10):
    smurf += random.choice(chars)

print(smurf)
