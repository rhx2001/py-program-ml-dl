s=input()
n=len(s)
dp=[[0]*(n+1) for i in range(n+1)]
s1=s[::-1]
for i in range(n):
    for j in range(n):
        if s[i]==s1[j]:
            dp[i+1][j+1]=max(dp[i][j]+1,dp[i+1][j+1])
        else:
            dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
print(n-dp[n][n])