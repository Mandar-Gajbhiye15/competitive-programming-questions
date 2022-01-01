t = int(input())
list1 = []
for _ in range(t):
    n = int(input())
    rev = str(n)[::-1]
    list1.append(int(rev))
for i in range(0,t):
    print(list1[i])




    