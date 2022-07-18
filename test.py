import random

def readlff(filename):
    with open(filename) as lr:
        lines = lr.readlines()

    random_line = random.choice(lines).strip() 
    return random_line

name = readlff("character_last_name.txt")

print(name)