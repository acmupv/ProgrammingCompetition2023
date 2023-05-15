import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N, D;
        int caseNum = 1;

        while (true) {
            N = scanner.nextInt();
            D = scanner.nextInt();

            if (N == 0 && D == 0) {
                break;
            }

            if (caseNum != 1) {
                System.out.println();
            }

            System.out.println("Caso " + caseNum + ":");
            Map<Integer, List<Integer>> banks = new HashMap<>();

            for (int i = 0; i < N; i++) {
                int money = scanner.nextInt();
                int P = scanner.nextInt();

                if (!banks.containsKey(P)) {
                    banks.put(P, new ArrayList<>());
                }

                banks.get(P).add(money);
            }

            alg(N, D, banks);

            caseNum++;
        }
    }

    public static void alg(int N, int D, Map<Integer, List<Integer>> banks) {
        List<Integer> sortedDangers = new ArrayList<>(banks.keySet());
        Collections.sort(sortedDangers);

        List<Integer> maxMoney = new ArrayList<>();
        for (int i : sortedDangers) {
            int sum = 0;
            for (int money : banks.get(i)) {
                sum += money;
            }
            maxMoney.add(sum);
        }

        int suma = 0;
        int danger = 0;

        while (suma < D && danger < sortedDangers.size()) {
            suma += maxMoney.get(danger);
            danger++;
        }

        if (suma < D) {
            System.out.println("impossible");
        } else {
            int[] numBanks = new int[danger];
            suma = 0;

            while (suma < D) {
                int maxim = 0;
                int level = 0;

                for (int i = 0; i < danger; i++) {
                    try {
                        List<Integer> dangerBanks = banks.get(sortedDangers.get(i));
                        int aux = Collections.max(dangerBanks);

                        if (aux > maxim) {
                            maxim = aux;
                            level = i;
                        }
                    } catch (NoSuchElementException e) {
                        // Ignore empty list
                    }
                }

                List<Integer> selectedBanks = banks.get(sortedDangers.get(level));
                selectedBanks.remove(Integer.valueOf(maxim));
                suma += maxim;
                numBanks[level]++;
            }

            for (int i = 0; i < danger; i++) {
                if (numBanks[i] != 0) {
                    System.out.println(sortedDangers.get(i) + " -> " + numBanks[i]);
                }
            }
        }
    }
}
