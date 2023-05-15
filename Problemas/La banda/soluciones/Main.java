import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        while (cases-- > 0){
            int people = sc.nextInt();
            int pairs = sc.nextInt();
            int max = 1;
            
            int[] array = new int[people]; 
            for(int i = 0; i < people; i++){
                array[i] = 0;
            }
            int numGroups = 1;
            Map<Integer, Integer> map = new HashMap<Integer, Integer>(); //Aquí guardaremos cuanta gente hay en cada grupo
            while(pairs-- > 0){
                int p1 = sc.nextInt() - 1;
                int p2 = sc.nextInt() - 1;
                int l1 = array[p1]; // grupo de l1
                int l2 = array[p2]; //grupo de l2
                
                if(l1 == 0 && l2 != 0) { //añadimos p1 a l2
                    array[p1] = l2;
                    map.put(l2, map.get(l2) + 1);


                } else if(l1 != 0 && l2 == 0) { //Añadimos p2 a l1
                    array[p2] = l1;
                    map.put(l1, map.get(l1) + 1);

                } else if(l1 == 0 && l2 == 0){ //Los dos son nulos -> Creamos un nuevo grupo
                    l1 = numGroups;
                    array[p2] = numGroups;
                    array[p1] = numGroups;
                    map.put(numGroups++, 2);
                    
                } else if(l1 != l2){ //Los dos tienen grupos -> Si son diferentes los unimos
                    for(int i = 0; i < people; i++){
                        if(array[i] == l2) {
                            array[i] = l1;
                        }
                    }
                    map.put(l1, map.get(l1) + map.get(l2));
                    map.remove(l2);
                    //System.out.println("Unidos grafos de " + p1 + " y " + p2);
                    
                } 
                //Calculamos el máximo
                if(map.get(l1) != null && map.get(l1) > max) max = map.get(l1);
                if(map.get(l2) != null && map.get(l2) > max) max = map.get(l2);

            }


            System.out.println(max);
        
        }

    }

}
