import math
r = str(math.factorial(int(input())))
q = 0
for c in r[::-1]:
    if c == '0':
        q += 1
    else:
        break
print(q)
