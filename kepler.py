import math
t = int(input())
result = []
for _ in range(t):
    T1,T2,R1,R2 = map(int, input().split())
    if ((math.pow(T1,2)/math.pow(R1,3)) == (math.pow(T2,2)/math.pow(R2,3))):
        result.append("Yes")
    else: 
        result.append("No")

print(*result, sep = "\n")