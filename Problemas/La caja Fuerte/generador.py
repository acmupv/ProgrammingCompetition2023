import random

val = 200000
print(val)
for i in range(val):
    print(random.randint(0, 1000))

for i in range(100000):
    ini = random.randint(1, val)
    print(f'M {ini} {random.randint(ini, val)}')
    if i % 2 == 0:
        print(f'S {random.randint(1, val)} {random.randint(0, 1000)}')

    ini = random.randint(1, val)
    print(f'M {ini} {random.randint(ini, val)}')

print('END')
print('0')