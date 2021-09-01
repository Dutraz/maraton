t = input()

a = ''
q, m = 1, 1

for c in t:
    if c == a:
        q += 1
        if q > m:
            m = q
    else:
        q = 1
    a = c

print(m)
