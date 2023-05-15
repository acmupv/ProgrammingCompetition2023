import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n;
        int[][] mat;

        while(sc.hasNextInt()) {
            n = sc.nextInt();
            mat = new int[n][n];
            //Rellenamos la matriz con los datos de entrada
            for (int i = 0; i < n; i++){
                for (int j = 0; j < n; j++){
                    mat[i][j] = sc.nextInt();
                }
            }

            System.out.println(maxSubRectangle(mat, n));
        }

        sc.close();

    }

    //Devuelve el máximo subRectángulo
    public static int maxSubRectangle(int[][] mat, int n){
        int max = Integer.MIN_VALUE;
        int[] values;
        for(int left = 0; left < n; left++) {
            values = new int[n];
            for (int right = left; right < n; right++){
                for(int row = 0; row < n; row++){
                    if(right == left) values[row] = mat[row][right]; //llenamos el array con los valores iniciales
                    else values[row] += mat[row][right]; //Calculamos el array actual
                }

                max = Math.max(max, kadane(values, n));
            }
        }
        return max;
    }

    //Devuelve la máxima suma del array
    public static int kadane(int[] values, int n) {
        int max = Integer.MIN_VALUE;
        int current = 0;
        for(int i = 0; i < n; i++){
            current += values[i];
            if(current < 0) {
                current = 0; //Como es menor que 0 lo reiniciamos
                max = Math.max(max, values[i]); //values[i] >= current
            } else max = Math.max(max, current);
        }

        return max;
    }

}
