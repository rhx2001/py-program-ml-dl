n=int(input())
prime=[0]*1001
b=[True]*1001
for i in range(2,1001):
    if b[i]:
        j=i
        while j*i<1001:
            b[i*j]=False
            j+=1

dp=[0]*1001
dp[0]=1
for i in range(2,1001):
    if b[i]:
        for j in range(i,1001):
            dp[j]=dp[j]+dp[j-i]
print(dp[n])


