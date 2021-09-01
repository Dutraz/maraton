for i in range(int(input())):
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    print((sum(v[:-1])/(n-1))+v[-1])
