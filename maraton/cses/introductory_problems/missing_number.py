n = int(input())
r = sum(map(int, input().split()))

# Fórmula da PA
s = n*(n+1)//2
print(s-r)
