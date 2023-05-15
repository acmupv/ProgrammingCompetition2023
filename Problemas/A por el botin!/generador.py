import random

for i in range(100):
    string = ''
    for i in range(100):
        string += str(random.randint(-200, 200)) + " "
    print(string.strip())
