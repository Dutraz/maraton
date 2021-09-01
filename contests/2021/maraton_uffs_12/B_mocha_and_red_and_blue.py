for _ in range(int(input())):
    n = int(input())
    s = list(input())

    fb = -1 if 'B' not in s else s.index('B')
    fr = -1 if 'R' not in s else s.index('R')
    i = fb if fb < fr and fb != -1 or fr == -1 else fr

    if(i == -1):
        s[0] = 'B'
    elif (i > 0):
        if (fb < fr and fb != -1 or fr == -1):
            s[0]='R' if i % 2 == 1 else 'B'
        else:
            s[0]='R' if i % 2 == 0 else 'B'

    for i in range(1, n):
        if (s[i] == '?'):
            s[i] = 'R' if s[i-1] == 'B' else 'B'

    print(''.join(s))
