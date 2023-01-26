from math import floor

n,k = input().split()
n,k = int(n),int(k)


i = 0

while i < k:
    n = n/2
    i += 1

print(floor(n))
