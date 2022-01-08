t = int(input())
ans = []
for i in range(t):
    a = list(map(int,input().split()))
    x = a[0]
    y = a[1]
    p = a[2]
    q = a[3]
    x1 = x + 10*p 
    y1 = y + 10*q
    if(x1<y1):
        ans.append("CHEF")
    elif(x1==y1):
        ans.append("DRAW")

    else:
        ans.append("CHEFINA")
for i in range(t):
    print(ans[i])