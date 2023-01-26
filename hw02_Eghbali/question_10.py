a = int(input())
b = int(input())

a+=1
num_list = []

factor_count=0

while a < b:
    for i in range(1,b):
        if a % i == 0:
            factor_count += 1
    if factor_count < 3:
        num_list.append(str(a))
        
    factor_count = 0
    a += 1

output = ",".join(num_list)
print(output)