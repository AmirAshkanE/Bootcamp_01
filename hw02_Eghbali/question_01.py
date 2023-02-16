k = int(input())

i = 1
num = 0
is_finished = False

while not is_finished:
    num += i
    j = 1
    factor_count = 0
    while j <= num:
        if num % j == 0:
            factor_count += 1
        j += 1
    if factor_count >= k:
        print(num)
        is_finished = True
    
    i+= 1
