import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args){
  
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        //PrintWriter out = new PrintWriter(System.out);
        int caso = 1;
        try{
            int nElementos = Integer.parseInt(br.readLine());
            while(nElementos != 0) {
                if(caso != 1) bw.write("\n");
                bw.write("Caso " + caso++ + ":\n");
                bw.flush();
                int[] valores = new int[nElementos];
                for (int i = 0; i < nElementos; i++){
                    valores[i] = Integer.parseInt(br.readLine()); //Leemos los valores iniciales
                }
                SegmentTree sg = new SegmentTree(valores);
                StringTokenizer st = new StringTokenizer(br.readLine()); //Para leer la linea
                String tok = st.nextToken(); //tok -> palabra actual
                while(!tok.equals("END")){
                    if(tok.equals("S")) { //Modificar
                        int i = Integer.parseInt(st.nextToken()) - 1;
                        sg.modify(i, Integer.parseInt(st.nextToken()));
                    }
                    else{ //Mostrar suma
                        bw.write(sg.minim(Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()) - 1) + "\n");
                    }
                    st = new StringTokenizer(br.readLine());
                    tok = st.nextToken();
                    bw.flush();
                }
                nElementos = Integer.parseInt(br.readLine());
                
            }
        }
        catch(IOException e) {}
    }
}

class Node{ //Clase para el nodo del arbol
    int start, end, val;
    public Node(int start, int end, int val){
        this.start = start;
        this.end = end;
        this.val = val;
    }
}
class SegmentTree{
    private int[] a;
    private int n;
    private int[] tree;
    public SegmentTree(int[] a) {
        this.a = a.clone();
        this.n = a.length;
        tree = new int[(n << 1) << 1]; //El árbol tendrá n * 4 nodos
        build(1, 0, this.n - 1); //Construimos el árbol
    }

    private void build(int node, int start, int end) {
        if(start == end) tree[node] = a[start]; 
        else{
            
            int mid = (start + end) >> 1; //(start + end) / 2
            int nodeL = node << 1; // node * 2
            int nodeR = (node << 1) + 1; //node * 2 + 1  
            build(nodeL, start, mid); //Construimos el nodo actual recursivamente, a partir de sus nodos hijo
            build(nodeR, mid + 1, end);

            tree[node] = Math.min(tree[nodeL], tree[nodeR]);
        }
    }

    public void modify(int i, int val){
        modify(1, 0, n - 1, i, val);
    }

    private void modify(int node, int start, int end, int i, int val){
        if(start == end && start == i) { //En el nodo del elemento simplemente cambiamos el valor
            tree[node] = val;
            a[i] = val;
        }
        else{
            int mid = (start + end) >> 1;
            int nodeL = node << 1;
            int nodeR = (node << 1) + 1;  
            if(i <= mid) modify(nodeL, start, mid, i, val); //Buscamos el nodo que tenemos que modificar, de forma recursiva
            else modify(nodeR, mid + 1, end, i, val);

            tree[node] = Math.min(tree[nodeL], tree[nodeR]); //Volvemos a calcular el valor
        }
    }

    public int minim(int i, int j){
        return minim(1, 0, n - 1, i, j);
    }

    private int minim(int node, int start, int end, int i, int j){
        if(start > j || end < i) return Integer.MAX_VALUE;
        if(i <= start && end <= j) return tree[node]; //Si esta dentro devolvemos el valor actual, caso base
        int mid = (start + end) >> 1;
        int nodeL = node << 1;
        int nodeR = (node << 1) + 1;  

        return  Math.min(minim(nodeL, start, mid, i, j), minim(nodeR, mid + 1, end, i, j)); //Devolvemos la suma recursiva


    }
}
