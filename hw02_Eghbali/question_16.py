n = int(input())

is_prime = False
factor_count = 0


for i in range(1,n+1):
    if n % i ==0:
        factor_count+=1
if factor_count < 3:
    is_prime = True

if is_prime:
    print(n)
else:
    print("ASK The Teacher")