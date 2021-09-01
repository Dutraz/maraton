n = int(input())

if n != 2 and n != 3:
    p = [j for j in range(1, n+1) if j % 2 == 0]
    i = [j for j in range(1, n+1) if j % 2 == 1]
    print(*p, *i)
else:
    print('NO SOLUTION')
