for j in range(int(input())):
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    s = 1
    for i in range(len(v)-1):
        if v[i] > v[i+1]:
            s += 1
    print('YES' if s <= k else 'NO')
