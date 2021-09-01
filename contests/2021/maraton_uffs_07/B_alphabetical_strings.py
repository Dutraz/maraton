for i in range(int(input())):
    s = input()

    if 'a' in s:
        li = s.index('a') - 1
        ri = s.index('a') + 1
        t = len(s)
        c = 97

        while True:
            c += 1

            l = '' if li < 0 else ord(s[li])
            r = '' if ri >= t else ord(s[ri])

            if l == '' and r == '':
                print('YES')
                break

            if l == c:
                li -= 1
            elif r == c:
                ri += 1
            else:
                print('NO')
                break

    else:
        print('NO')
