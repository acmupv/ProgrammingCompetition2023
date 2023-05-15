import sys

# Devuelve la máxima suma del array
def kadane(values):
    n = len(values)
    max_sum = float('-inf')
    current_sum = 0
    for i in range(n):
        current_sum += values[i]
        if current_sum < 0:
            current_sum = 0  # Como es menor que 0 lo reiniciamos
            max_sum = max(max_sum, values[i])  # values[i] >= current_sum
        else:
            max_sum = max(max_sum, current_sum)
    return max_sum


# Devuelve el máximo subRectángulo
def maxSubRectangle(mat, n):
    max_rect = float('-inf')
    for left in range(n):
        values = [0] * n
        for right in range(left, n):
            for row in range(n):
                if right == left:
                    values[row] = mat[row][right]  # llenamos el array con los valores iniciales
                else:
                    values[row] += mat[row][right]  # Calculamos el array actual

            max_rect = max(max_rect, kadane(values))

    return max_rect


if __name__ == "__main__":
    for line in sys.stdin:
        n = int(line)
        mat = []
        # Rellenamos la matriz con los datos de entrada
        for i in range(n):
            row = list(map(int, input().split()))
            mat.append(row)

        print(maxSubRectangle(mat, n))
