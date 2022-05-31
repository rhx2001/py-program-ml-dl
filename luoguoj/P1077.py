n,m =map(int, input().split())
a=[0]+[int(i) for i in input().split()]
dp=[[0]*(m+1) for i in range(n+1)]
for i in range(n):
    dp[i][0]=1
for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(min(j,a[i])+1):
            dp[i][j]=(dp[i-1][j-k]+dp[i][j])%int(1e6+7)
# print(dp)
print(dp[n][m])