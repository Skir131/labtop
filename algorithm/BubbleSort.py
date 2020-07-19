T = int(input())
result = []
for i in range(T):
    a = int(input())
    result.insert(i, a)

result.sort()

for j in range(len(result)-1):
    for k in range(len(result)-j-1):
        if result[j] > result[j+1]:
            result[j], result[j+1] = result[j+1], result[j]

for i in range(T):
    print(result[i])