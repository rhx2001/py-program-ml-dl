t,n,mon=map(int,input().split())
a=[]
for j in range(t):
    a.append([int(x) for x in input().split()])
nums=mon
# print(a)
for i in range(t-1):
    dp = [0] * (nums+1)
    dp[nums]=nums
    for j in range(n):
        for k in range(nums,a[i][j]-1,-1):
            dp[k-a[i][j]]=max(dp[k-a[i][j]],dp[k]+a[i+1][j]-a[i][j])#指的是max(不买明天得到的收入，买了明天的收入)
    nums=max(nums,max(dp))
print(nums)