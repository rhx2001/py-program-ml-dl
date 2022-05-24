n=int(input())
a=[]
for i in range(n):
    s=int(input())
    a.append(s)
dp=[[0]*n for i in range(n)]
for i in range(n):
    dp[i][i]=a[i]*n
# print(dp)
for i in range(2,n+1):
    for j in range(n):
        r=j+i-1
        if r>=n:break
        dp[j][r]=max(dp[j][r-1]+a[r]*(n-i+1),dp[j+1][r]+a[j]*(n-i+1))
print(dp[0][n-1])