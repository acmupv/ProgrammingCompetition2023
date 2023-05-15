#include <bits/stdc++.h>
using namespace std;

//Declaramos las funciones
long long maxSubRectangle(vector<vector<long long>>& mat, int n);
long long kadane(vector<long long>& values, int n);

int main() {
    int n;
    vector<vector<long long>> mat;

    while(cin >> n) {
        mat.resize(n, vector<long long>(n));

        //Rellenamos la matriz con los datos de entrada
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                cin >> mat[i][j];
            }
        }

        cout << maxSubRectangle(mat, n) << endl;
    }

    return 0;
}

//Devuelve el máximo subRectángulo
long long maxSubRectangle(vector<vector<long long>>& mat, int n) {
    long long maxim = INT32_MIN;
    vector<long long> values(n);
    for(int left = 0; left < n; left++) {
        fill(values.begin(), values.end(), 0);
        for (int right = left; right < n; right++){
            for(int row = 0; row < n; row++){
                if(right == left) values[row] = mat[row][right]; //llenamos el array con los valores iniciales
                else values[row] += mat[row][right]; //Calculamos el array actual
            }

            maxim = max(maxim, kadane(values, n));
        }
    }
    return maxim;
}

//Devuelve la máxima suma del array
long long kadane(vector<long long>& values, int n) {
    long long maxim = INT32_MIN;
    long long current = 0;
    for(int i = 0; i < n; i++){
        current += values[i];
        if(current < 0) {
            current = 0; //Como es menor que 0 lo reiniciamos
            maxim = max(maxim, values[i]); //values[i] >= current
        } else maxim = max(maxim, current);
    }

    return maxim;
}
