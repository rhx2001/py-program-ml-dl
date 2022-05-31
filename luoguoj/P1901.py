n=int(input())
a=[int(i) for i in input().split()]
dp1=[1]*(n+1)
dp2=[1]*(n+1)
for i in range(1,n):
    for j in range(i):
        if a[j]<a[i]:
            dp1[i]=max(dp1[i],dp1[j]+1)

for i in range(n-2,-1,-1):
    for j in range(i+1,n):
        if a[j]<a[i]:
            dp2[i]=max(dp2[i],dp2[j]+1)

ans=0
for i in range(n):
    ans=max(dp1[i]+dp2[i]-1,ans)
print(n-ans)