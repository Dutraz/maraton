def dist(p1, p2, pf, a, b, c):
    a, b = (a, b) if a > b else (b, a)
    if p1 != p2:
        return abs(p1-p2)
    elif p1 == pf and c < a and c > b:
        return 2
    return 0


for i in range(int(input())):
    input()
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xf, yf = map(int, input().split())

    print(dist(xa, xb, xf, ya, yb, yf) + dist(ya, yb, yf, xa, xb, xf))
