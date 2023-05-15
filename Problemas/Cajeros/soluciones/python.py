def main():
    # Leer el límite de tiempo
    limiteTiempo = int(input())

    # Leer las cantidades de dinero
    s_dinero = input().split(" ")

    # Leer los tiempos de apertura
    s_tiempo = input().split(" ")

    # Obtener el número de cajas fuertes
    n = len(s_dinero)

    # Dinero to array
    dinero = [int(x) for x in s_dinero]

    # Tiempo to array
    tiempo = [int(x) for x in s_tiempo]

    # Inicializar la matriz de valores óptimos
    valorOptimo = [[0] * (limiteTiempo + 1) for _ in range(n + 1)]

    # Calcular los valores óptimos para cada subconjunto de cajas fuertes y tiempo
    for i in range(1, n + 1):
        for j in range(limiteTiempo + 1):
            if tiempo[i - 1] <= j:
                valorOptimo[i][j] = max(valorOptimo[i - 1][j], dinero[i - 1] + valorOptimo[i - 1][j - tiempo[i - 1]])
            else:
                valorOptimo[i][j] = valorOptimo[i - 1][j]

    # Obtener las cajas fuertes que proporcionan la mayor cantidad de dinero
    j = limiteTiempo
    cajasOptimas = []
    for i in range(n, 0, -1):
        if valorOptimo[i][j] != valorOptimo[i - 1][j]:
            cajasOptimas.append(i - 1)
            j -= tiempo[i - 1]
    cajasOptimas.reverse()

    # Imprimir los resultados
    print(limiteTiempo - j)
    print(" ".join(str(caja + 1) for caja in cajasOptimas))
    print(valorOptimo[n][limiteTiempo])

if __name__ == "__main__":
    main()
