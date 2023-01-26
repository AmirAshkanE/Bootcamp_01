a = int(input())
b = int(input())

factor_count = 0


if a == 1 and b == 1:
    pass
elif a == 1 and b == 2:
    print(2)
elif a == 2 and b == 2:
    print(2)
else:
    if a==1:
        a=2
    
    while a <= b:
        for i in range(1,b+1):
            if a % i == 0:
                factor_count += 1
        if factor_count < 3:
            print(a)
        
        factor_count = 0
        a += 1

