a, b, c = map(int, input().split()) 

min_value = min(a, b, c)

if a == min_value:
    res1 = 1
else:
    res1 = 0

if a == b and b == c:
    res2 = 1
else:
    res2 = 0

print(res1, res2)