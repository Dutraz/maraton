n = int(input())
v = list(map(int, input().split()))

p = 0
for i in range(1, n):
    if v[i] < v[i-1]:
        p += v[i-1] - v[i]
        v[i] = v[i-1]

print(p)
