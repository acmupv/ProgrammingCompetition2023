#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

void alg(int N, int D, map<int, vector<int>>& banks);

int main() {
    int N, D;
    int caseNum = 1;

    while (true) {
        cin >> N >> D;

        if (N == 0 && D == 0) {
            break;
        }

        if (caseNum != 1) {
            cout << endl;
        }

        cout << "Caso " << caseNum << ":" << endl;
        map<int, vector<int>> banks;

        for (int i = 0; i < N; i++) {
            int money, P;
            cin >> money >> P;

            if (banks.find(P) == banks.end()) {
                banks[P] = vector<int>();
            }

            banks[P].push_back(money);
        }

        alg(N, D, banks);

        caseNum++;
    }

    return 0;
}

void alg(int N, int D, map<int, vector<int>>& banks) {
    vector<int> sortedDangers;
    for (const auto& entry : banks) {
        sortedDangers.push_back(entry.first);
    }
    sort(sortedDangers.begin(), sortedDangers.end());

    vector<int> maxMoney;
    for (int i : sortedDangers) {
        int sum = 0;
        for (int money : banks[i]) {
            sum += money;
        }
        maxMoney.push_back(sum);
    }

    int suma = 0;
    int danger = 0;

    while (suma < D && danger < sortedDangers.size()) {
        suma += maxMoney[danger];
        danger++;
    }

    if (suma < D) {
        cout << "impossible" << endl;
    } else {
        vector<int> numBanks(danger, 0);
        suma = 0;

        while (suma < D) {
            int maxim = 0;
            int level = 0;

            for (int i = 0; i < danger; i++) {
                try {
                    vector<int>& dangerBanks = banks[sortedDangers[i]];
                    int aux = *max_element(dangerBanks.begin(), dangerBanks.end());

                    if (aux > maxim) {
                        maxim = aux;
                        level = i;
                    }
                } catch (const out_of_range& e) {
                    // Ignore empty list
                }
            }

            vector<int>& selectedBanks = banks[sortedDangers[level]];
            selectedBanks.erase(find(selectedBanks.begin(), selectedBanks.end(), maxim));
            suma += maxim;
            numBanks[level]++;
        }

        for (int i = 0; i < danger; i++) {
            if (numBanks[i] != 0) {
                cout << sortedDangers[i] << " -> " << numBanks[i] << endl;
            }
        }
    }
}
