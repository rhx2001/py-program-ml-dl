a,b,c=map(int,input().split())
润1=0
润掉=0
for i in range(1,c+1):
    润掉 += 17
    if a>=10:
        润1+=60
        a-=10
    else:a+=4
    if 润1>润掉:
        润掉=润1
    # print(润掉,润1,润2)
    if 润掉>=b:
        print("Yes")
        print(i)
        break
if 润掉<b:
    print("No")
    print(润掉)

# a,b,c=map(int,input().split())
# 润1=0
# 润掉=0
# for i in range(c):
#     run += 17
#     if a>=10:
#         flash+=60
#         a-=10
#     else:a+=4
#     run=max(flash,run)
#     # print(润掉,润1,润2)
#     if run>=b:
#         print("YES")
#         print(i+1)
#         break
# if run<b:
#     print("No")
#     print(run)