#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    string last_magnet = "";
    int groups = 0;

    for (int i = 0; i < n; i++) {
        string magnet;
        cin >> magnet;

        if (magnet != last_magnet) {
            groups++;
            last_magnet = magnet;
        }
    }

    cout << groups;
}