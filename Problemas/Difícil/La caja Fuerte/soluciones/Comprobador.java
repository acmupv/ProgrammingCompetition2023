import java.io.*;
import java.util.*;

public class Comprobador {
    public static void main(String[] args) {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // PrintWriter out = new PrintWriter(System.out);
        int caso = 1;
        try {
            int nElementos = Integer.parseInt(br.readLine());
            while (nElementos != 0) {
                if (caso != 1)
                    bw.write("\n");
                bw.write("Caso " + caso++ + ":\n");
                bw.flush();
                int[] valores = new int[nElementos];
                for (int i = 0; i < nElementos; i++) {
                    valores[i] = Integer.parseInt(br.readLine()); // Leemos los valores iniciales
                }
                StringTokenizer st = new StringTokenizer(br.readLine()); // Para leer la linea
                String tok = st.nextToken(); // tok -> palabra actual
                while (!tok.equals("END")) {
                    if (tok.equals("S")) { // Modificar
                        int i = Integer.parseInt(st.nextToken()) - 1;
                        valores[i] = Integer.parseInt(st.nextToken());
                    } else { // Mostrar suma
                        int ini = Integer.parseInt(st.nextToken()) - 1;
                        int fi = Integer.parseInt(st.nextToken());
                        int min = Integer.MAX_VALUE;
                        for (int i = ini; i < fi; i++) {

                            min = Math.min(min, valores[i]);
                        }
                        bw.write(min + "\n");
                    }
                    st = new StringTokenizer(br.readLine());
                    tok = st.nextToken();
                    bw.flush();
                }
                nElementos = Integer.parseInt(br.readLine());

            }
        } catch (IOException e) {
        }
    }
}
