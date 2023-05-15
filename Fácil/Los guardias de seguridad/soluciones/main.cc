#include <bits/stdc++.h>
using namespace std;

int main() {
    /* // GENERATOR
    std::random_device rd;
    std::mt19937 rng(rd());
    std::uniform_int_distribution<int> uniP(1,1000);
    std::uniform_int_distribution<int> uniN(-1000000000,1000000000);

    int tt = 1000;
    cout << tt << endl;
    for (int t = 0; t < tt; ++t) {
        int n = 1000;
        cout << n << endl;
        for (int nn = 0; nn < n; ++nn) {
            cout << uniN(rng) << ' ';
        }
        cout << endl;
    }*/

    // ANS
    int tt, in; cin >> tt;
    for (int t = 1; t <= tt; ++t) {
        int n; cin >> n;
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            cin >> in;
            if (in > 0) ans += in;
        }
        cout << "Caso " << t << ": " << ans << endl;
    }
    return 0;
}