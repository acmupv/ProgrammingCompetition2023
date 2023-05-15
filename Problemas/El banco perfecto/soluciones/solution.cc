#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define entf cout << endl
#define ent cout << "\n"
#define REP(i, a, b) for (int i = a; i < b; ++i)
#define REPV(i, a, b) for (int i = a; i >= b; --i)
#define MOD 1000000007

#define srt(v) sort(v.begin(), v.end())
#define rsrt(v) sort(v.rbegin(), v.rend())
#define s() size()
/*print table*/
/*substring*/
/*sort multiple*/
/*shift array*/
/*memset*/

#define TESTCASES true
void solve(int tt) {
	// Entrada de datos para un caso individual
	int n; cin >> n;
	char a[n]; REP(i, 0, n) cin >> a[i];
	// Array vacio (numeros random, no dara errores)
	int dp[n];
	// Usando dp, calculamos la distancia entre policia y bancos, de izquierda a derecha
	int idx = 100000;
	REP(i, 0, n) {
		if (a[i] == 'P') idx = 0;
		dp[i] = idx++;
	}
	// Y ahora actualizamos la distancia si de derecha a izquierda hay un policia mas cercano
	// Sobreescribimos cada vez que hay un banco la respuesta en ans
	idx = n;
	int ans = INT32_MIN;
	REPV(i, n-1, 0) {
		idx++;
		if (a[i] == 'P') idx = 0;
		if (a[i] == 'B') ans = max(min(dp[i], idx), ans);
	}
	// Imprimimos la distancia + 10 (minutos de margen extra del enunciado)
	cout << 10 + ans; ent;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	// freopen("problemname.in", "r", stdin);
	// freopen("problemname.out", "w", stdout);

	if (TESTCASES) {
		int tt; cin >> tt; 
		REP(i, 1, tt+1) {
			// cout << "#CASE " << i;
			solve(i);
		}
	} else solve(1);

    return 0;
}
