n = int(input())

for i in range(1,n):
    power = 2**i
    if power > n:
        print(power)
        break
    