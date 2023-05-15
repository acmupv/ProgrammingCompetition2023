import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        if (TESTCASES) {
            int tt = scanner.nextInt();
            for (int i = 1; i <= tt; i++) {
                solve(i, scanner);
            }
        } else {
            solve(1, scanner);
        }

        scanner.close();
    }

    static void solve(int tt, Scanner scanner) {
        // Entrada de datos para un caso individual
        int n = scanner.nextInt();
        String a = scanner.next();
        
        // Array vacío (números aleatorios, no dará errores)
        int[] dp = new int[n];
        // Usando dp, calculamos la distancia entre policía y bancos, de izquierda a derecha
        int idx = 100000;
        for (int i = 0; i < n; i++) {
            if (a.charAt(i) == 'P') {
                idx = 0;
            }
            dp[i] = idx++;
        }
        // Y ahora actualizamos la distancia si de derecha a izquierda hay un policía más cercano
        // Sobreescribimos cada vez que hay un banco la respuesta en ans
        idx = n;
        int ans = Integer.MIN_VALUE;
        for (int i = n - 1; i >= 0; i--) {
            idx++;
            if (a.charAt(i) == 'P') {
                idx = 0;
            }
            if (a.charAt(i) == 'B') {
                ans = Math.max(Math.min(dp[i], idx), ans);
            }
        }
        // Imprimimos la distancia + 10 (minutos de margen extra del enunciado)
        System.out.println(10 + ans);
    }

    static final boolean TESTCASES = true;
}

  

        

            
                               
                                

              
          

     

 

       
            
         

                     
             
                 
                    
             
             

          
                                                                                           // 

    