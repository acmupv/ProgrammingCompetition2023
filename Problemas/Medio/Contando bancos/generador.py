import random

for i in range(3):
    banks = random.randint(10, 50)
    money = random.randint(500, 10000)
    print(f'{banks} {money}')
    for i in range(banks):
        print(f'{random.randint(200, 3000)} {random.randint(1, 5)}')

print('0 0')