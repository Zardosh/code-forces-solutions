#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    int participants[n];

    cin >> n >> k;

    for (int i = 0; i < n; i++) {
        int participant;
        cin >> participant;
        
        participants[i] = participant;
    }
    
    k = participants[k - 1];

    int total = 0;

    for (int i = 0; i < n; i++) {
        if (participants[i] >= k && participants[i] > 0) {
            total++;
        }
    }

    cout << total;
}