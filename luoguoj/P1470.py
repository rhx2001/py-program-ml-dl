# a=[set() for i in range(13)]
a=[]
strs=' '
m=0
dp=[0]*10001
while True:
    s=[i for i in input().split()]
    if s[0] == '.':
        break
    for i in s:
        a.append(i)
        m=max(m,len(i))
while True:
    try:
        # print("?")
        s=input()
        # if s==".":break
        strs+=s[:-1]
        # break
    except:
        break
n=len(strs)
dp[0]=1
ans=0
i=1
while i<n:
    for j in range(min(i,m),0,-1):
        # print(strs[i-j+1:i+1],i,j)
        if strs[i-j+1:i+1] in a and dp[i-j]==1:
            dp[i]=1
            ans=i
    i+=1
print(ans)

'''
A AB BA CA BBC
.
ABABACABAABC
'''