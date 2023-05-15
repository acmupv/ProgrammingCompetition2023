import java.util.*;

public class Cajeros {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        // Leer el límite de tiempo
        int limiteTiempo = input.nextInt();
        input.nextInt(); //Nada

        input.nextLine();
        
        // Leer las cantidades de dinero 
        String[] s_dinero = input.nextLine().split(" ");
        
        // Leer los tiempos de apertura
        String[] s_tiempo = input.nextLine().split(" ");
        
        // Obtener el número de cajas fuertes
        int n = s_dinero.length;
        
        // Dinero to array
        int[] dinero = new int[n];
        for (int i = 0; i < n; i++) {
            dinero[i] = Integer.parseInt(s_dinero[i]);
        }

        // for (int x : dinero) {
        //     System.out.print(x);
        // }

        // Tiempo to array
        int[] tiempo = new int[n];
        for (int i = 0; i < n; i++) {
            tiempo[i] = Integer.parseInt(s_tiempo[i]);
        }
        

        // Inicializar la matriz de valores óptimos
        int[][] valorOptimo = new int[n + 1][limiteTiempo + 1];
        
        // Calcular los valores óptimos para cada subconjunto de cajas fuertes y tiempo
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= limiteTiempo; j++) {
                if (tiempo[i-1] <= j) {
                    valorOptimo[i][j] = Math.max(valorOptimo[i-1][j], dinero[i-1] + valorOptimo[i-1][j-tiempo[i-1]]);
                } else {
                    valorOptimo[i][j] = valorOptimo[i-1][j];
                }
            }
        }
        
        // Obtener las cajas fuertes que proporcionan la mayor cantidad de dinero
        int j = limiteTiempo;
        List<Integer> cajasOptimas = new ArrayList<>();
        for (int i = n; i > 0 && j >= 0; i--) {
            if (valorOptimo[i][j] != valorOptimo[i-1][j]) {
                cajasOptimas.add(i-1);
                j -= tiempo[i-1];
            }
        }
        Collections.reverse(cajasOptimas);
        
        // Imprimir los resultados
        System.out.println(limiteTiempo - j);

        for (int caja : cajasOptimas) {
            System.out.print(caja + 1 + " ");
        }
        System.out.println("");
        System.out.println(valorOptimo[n][limiteTiempo]);
        input.close();
    }
}
