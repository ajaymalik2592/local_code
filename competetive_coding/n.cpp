#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    long long n;
    cin >> n;
    
    vector<long long > a(n);
    vector<long long> prefix(n + 1, 0LL);  // Use long long to avoid overflow
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        prefix[i+1] = prefix[i] + a[i];  // Cumulative sum stored in prefix
    }

    vector<vector<long long>> dp(n + 1, vector<long long>(n + 1, 0));  // Long long for dp as well

    // Bottom-up DP computation
    for (int l = n-1; l >= 0; --l) {
        for (int r = l+1; r < n; ++r) {
            long long s = prefix[r+1] - prefix[l];  // Sum from l to r
            dp[l][r] = min(dp[l+1][r], dp[l][r-1]) + s;

            // Try different splits to minimize the result
            for (int z = l+1; z < r; ++z) {
                dp[l][r] = min(dp[l][r], s + dp[l][z] + dp[z+1][r]);
            }

            // Debug output to track progress
            // cout << "dp[" << l << "][" << r << "] = " << dp[l][r] << endl;
        }
    }

    cout << dp[0][n-1] << endl;  // Output the final answer

    return 0;
}
