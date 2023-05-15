import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args){
        try {
            BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

            long vida = Long.parseLong(bf.readLine().trim());

            bf.readLine(); //Linea vacía
            String linea;
            long total = 0;
            long suma = 0;
            while (bf.ready()){
                linea = bf.readLine().trim();
                if (linea.isEmpty()) { //Si hay una linea vacía cambiamos de empleado
                    
                    if (suma >= vida){
                        total += suma; 
                    }
                    //System.out.prlongln("Suma " + suma + "//// total: " + total);
                        suma = 0;
                } else{
                    suma += Long.parseLong(linea);
                }
            } 

            if (suma >= vida){ //Como no termina con linea vacía tenemos que comprobarlo fuera otra vez
                total+= suma;         
            } 

            System.out.println(total);
            
        } catch (IOException e){
            
        }
    }
}