j = list(map(int, input().split()))
n = j[0]
k = j[1]
i = 0
while i < int(k):
    n = str(n)
    if n.endswith('0'):
        n = int(n) / 10
        n = int(n)
    else:
        n = int(n) - 1
    i += 1
print(n)

