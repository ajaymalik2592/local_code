n = int(input())
a = list(map(int, input().split()))
dp = [[0] * (n+1) for _ in range(n+1)]
for x in range(n):
    dp[x][x] = a[x]
for l in range(n-1, -1, -1):
    for r in range(l+1, n):
        dp[l][r] = max(a[l] - dp[l+1][r], a[r] - dp[l][r-1])
print(dp[0][n-1])
