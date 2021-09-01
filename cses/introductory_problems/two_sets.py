n = int(input())

v = [j for j in range(1, n+1)]

if sum(v) % 2:
    print('NO')
else:
    print('YES')
    if len(v) % 2:
        v = [0] + v
    q = len(v) // 4
    v1 = v[:q] + v[3*q:]
    v2 = v[q:3*q]

    if 0 in v1:
        v1.remove(0)

    print(len(v1))
    print(*v1)
    print(len(v2))
    print(*v2)
