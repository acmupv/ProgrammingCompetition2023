#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    
    for (int t = 0; t < cases; t++) {
        int people, pairs;
        cin >> people >> pairs;
        int max_val = 1;
        
        vector<int> array(people, 0);
        int numGroups = 1;
        unordered_map<int, int> map;
        
        for (int i = 0; i < pairs; i++) {
            int p1, p2;
            cin >> p1 >> p2;
            int l1 = array[p1 - 1];
            int l2 = array[p2 - 1];
            
            if (l1 == 0 && l2 != 0) {
                array[p1 - 1] = l2;
                map[l2] = map[l2] + 1;
            } else if (l1 != 0 && l2 == 0) {
                array[p2 - 1] = l1;
                map[l1] = map[l1] + 1;
            } else if (l1 == 0 && l2 == 0) {
                l1 = numGroups;
                array[p2 - 1] = numGroups;
                array[p1 - 1] = numGroups;
                map[numGroups] = 2;
                numGroups++;
            } else if (l1 != l2) {
                for (int j = 0; j < people; j++) {
                    if (array[j] == l2) {
                        array[j] = l1;
                    }
                }
                map[l1] = map[l1] + map[l2];
                map.erase(l2);
            }
            
            if (map[l1] > max_val) {
                max_val = map[l1];
            }
            if (map[l2] > max_val) {
                max_val = map[l2];
            }
        }
        
        cout << max_val << endl;
    }
    
    return 0;
}
