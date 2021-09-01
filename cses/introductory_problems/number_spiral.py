for i in range(int(input())):
    x, y = map(int, input().split())

    a, m, n = (-1, x, y) if x >= y else (1, y, x)
    o = (-1) ** (m % 2) * a
    d = m**2 - m+1

    print(d-o*(m-n))
