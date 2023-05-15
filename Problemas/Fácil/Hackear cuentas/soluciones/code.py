# Select ./input.txt and split it by \n


# # Read the file
# with open('input.txt', 'r') as file:
#     # Split the file by \n
#     data = file.read().split('\n')

data = [] # Temporary list
while(True):
    try:
        data.append(input().strip()) # Append to temporary list
    except EOFError:
        break
    

if (data[len(data) - 1] != ''): # If the last line is not empty
    data.append('') # Add an empty line


# Variables
VIDA = int(data[0])
EQUIPO = []
TORNEO = 0

# Reorder the list

for i in range(2, len(data)):
    if (data[i] == ''):
        suma = 0
        for j in EQUIPO:
            suma += int(j)

        if (suma >= VIDA):
            TORNEO += suma

        EQUIPO = []
    else:
        EQUIPO.append(data[i])

# Print the result
print(TORNEO)


# Zheng Lin Lei
# https://github.com/ZhengLinLei