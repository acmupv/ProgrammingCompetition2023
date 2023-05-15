import java.util.*;

class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int casos = sc.nextInt();
        for (int i = 1; i <= casos; i++){
            int el = sc.nextInt();

            long suma = 0;

            while(el-- > 0){
                long val = sc.nextInt();
                suma += val > 0 ? val : 0; //Si val > 0 lo sumamos
            }

            System.out.println("Caso " + i + ": " + suma);
        }
    }
}