#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
ld = number % 10
first_part = f"Last digit of {number} is {ld}"
if ld > 5:
    print(f"{first_part} and is greater than 5")
elif ld < 6:
    print(f"{first_part} and is less than 6 and not 0")
else:
    print(f"{first_part} and is 0")