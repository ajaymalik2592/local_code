#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;

int add(int a, int b) {
    int s = a + b;
    if (s >= MOD) {
        s -= MOD;
    }
    return s;
}

int n;
vector<vector<int>> matrix;
vector<int> dp;

int solve(int mask) {
    if (mask == (1 << n) - 1) {
        return 1;  // If all are assigned, return 1
    }

    if (dp[mask] != -1) {
        return dp[mask];  // If the result is already computed, return it
    }

    int ans = 0;
    int counter = __builtin_popcount(mask);  // Count the number of 1's (assigned persons)

    for (int x = 0; x < n; ++x) {
        if ((mask & (1 << x)) == 0 && matrix[counter][x] == 1) {
            ans = add(ans, solve(mask | (1 << x)));
        }
    }

    dp[mask] = ans;
    return ans;
}

int main() {
    cin >> n;

    matrix.resize(n, vector<int>(n));
    dp.resize(1 << n, -1);  // Initialize dp array with -1 (uncomputed)
    char c;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> c;
            if (c == '1'){
                matrix[i][j] =1;
            }else{
                matrix[i][j] = 0;
            }
        }
    }

    cout << solve(0) << endl;

    return 0;
}
