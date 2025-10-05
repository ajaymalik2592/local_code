n = int(input())
a = list(map(int, input().split()))
dp = [[0] * (n+1) for _ in range(n+1)]

prefix = [0 for x in range(n+1)]
for x in range(n):
    prefix[x+1] = prefix[x] + a[x]

for l in range(n-1, -1, -1):
    for r in range(l+1, n):
        s = prefix[r+1] - prefix[l]
        dp[l][r] =  min(dp[l+1][r], dp[l][r-1]) + s
        for z in range(l+1,r):
            if z == r:
                continue
            additional = s + min(prefix[z+1]- prefix[l], prefix[r+1] - prefix[z])
            val = dp[l][z-1] + dp[z+1][r]
            dp[l][r] = min(dp[l][r], val + additional)
# print(dp)
print(dp[0][n-1])
