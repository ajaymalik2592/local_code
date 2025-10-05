n = int(input())
matrix = []

mod = int ( 1e9 + 7 )

def add(a, b):
    s = a+b
    if s > mod:
        s -= mod
    return s


for x in range(n):
    s = input()
    s = [int(x) for x in s.split()]
    matrix.append(s)

dp = [None for x in range(1<<n)]

taken = [False for x in range(n)]
global counter 
counter= 0 
# print(matrix)
def solve(mask)->int:
    global counter
    if counter == n:
        return 1
    exist = dp[mask]
    if exist != None:
        return dp[mask]
    ans = 0
    for x in range(n):
        if (mask & (1<<x)) == 0 and matrix[counter][x]:
            counter +=1
            ans = add(ans, solve(mask|(1<<x)))
            counter -=1
    dp[mask] = ans
    return ans
    
solve(0)
# print(dp)
print(dp[0])