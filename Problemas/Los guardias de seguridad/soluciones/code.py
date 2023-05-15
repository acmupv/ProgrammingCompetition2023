casos = int (input())

for case in range(casos):
    input() #Número de elementos en la siguiente lista (No útil en python)

    arr = list(map(int, input().split()))

    suma = 0

    for i in arr:
        if i > 0:
            suma += i
    
    print(f'Caso {case + 1}: {suma}')