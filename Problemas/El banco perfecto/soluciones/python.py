TESTCASES = True

def solve(tt):
    # Entrada de datos para un caso individual
    n = int(input())
    a = input()
    # Array vacío (números aleatorios, no dará errores)
    dp = [0] * n
    # Usando dp, calculamos la distancia entre policía y bancos, de izquierda a derecha
    idx = 100000
    for i in range(n):
        if a[i] == 'P':
            idx = 0
        dp[i] = idx
        idx += 1
    # Y ahora actualizamos la distancia si de derecha a izquierda hay un policía más cercano
    # Sobreescribimos cada vez que hay un banco la respuesta en ans
    idx = n
    ans = float('-inf')
    for i in range(n - 1, -1, -1):
        idx += 1
        if a[i] == 'P':
            idx = 0
        if a[i] == 'B':
            ans = max(min(dp[i], idx), ans)
    # Imprimimos la distancia + 10 (minutos de margen extra del enunciado)
    print(10 + ans)

if __name__ == '__main__':
    if TESTCASES:
        tt = int(input())
        for i in range(1, tt + 1):
            solve(i)
    else:
        solve(1)
