# n, k = [int(x) for x in input().split()]
# a = [int(x) for x in input().split()]
# modulo = int(1e9 + 7)
# def add(a,b):
#     s = a+b
#     if s >= modulo:
#         s -= modulo
#     return s

# def sub(a, b):
#     s = a-b
#     if s < 0:
#         s+=modulo
#     return s

# dp = [0]*(k+1)
# dp[0] = 1
# for val in a:
#     dp1 = [0] * (k+1)
#     dp1[0] = dp[0]
#     for x in range(1, k+1):
#         dp1[x] = add(dp1[x-1], dp[x])
#     for x in range(k+1):
#         dp[x] = dp1[x]
#         if x-val-1>= 0:
#             dp[x] = sub(dp[x], dp1[x-val-1])
# print(dp[k]) 

n, k = map(int, input().split())
a = list(map(int, input().split()))
modulo = int(1e9 + 7)

dp = [0] * (k + 1)
dp[0] = 1

for val in a:
    pref = [0] * (k + 2)  # Extra 1 to avoid boundary issues
    for i in range(k+1):
        pref[i+1] = (pref[i] + dp[i]) % modulo
    for i in range(k+1):
        dp[i] = pref[i+1]
        if i - val >= 0:
            dp[i] = (dp[i] - pref[i-val] + modulo) % modulo
        if dp[i] == 0:
            break
print(dp[k])

