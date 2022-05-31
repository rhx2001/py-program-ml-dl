v,n=map(int,input().split())
a=[[0]*1001 for i in range(1001)]
zu=[0]*1001
val=[0]*1001
wig=[0]*1001
tmp=0
for i in range(n):
    t,b,c=map(int,input().split())
    tmp=max(tmp,c)
    val[i]=b
    wig[i]=t
    zu[c]+=1
    a[c][zu[c]]=i
dp=[0]*1001
for i in range(1,tmp+1):
    for j in range(v,-1,-1):
        for k in range(1,zu[i]+1):
            if j>=wig[a[i][k]]:dp[j]=max(dp[j],dp[j-wig[a[i][k]]]+val[a[i][k]])
print(dp[v])

'''
10 3
5 5 1
4 1 1
6 100 2
'''

ord("a")
ord("b")
