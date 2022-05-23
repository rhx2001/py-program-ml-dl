n=int(input())
a=[[0]*200 for i in range(200)]
for j in range(n-1):
    t=[int(i) for i in input().split()]
    num=0
    for k in range(j+1,n):
        a[j][k]=t[num]
        num+=1
ans=0
dp=[float("inf")]*(n+1)
dp[0]=0
for i in range(n):
    for j in range(i+1,n):
        dp[j]=min(dp[j],dp[i]+a[i][j])
print(dp[n-1])

'''
3
5 15
7


'''
