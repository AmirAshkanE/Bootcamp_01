num_list = []
for i in range(1, 5):
    a = float(input())
    num_list.append(a)

sum = 0
num_product = 1
for i in num_list:
    sum += i
    num_product *= i


average = sum/len(num_list)
max_num = max(num_list)
min_num = min(num_list)

print(f"Sum : {sum:.6f} \nAverage : {average:.6f} \nProduct : {num_product:.6f}\nMAX : {max_num:.6f}\nMIN : {min_num:.6f}")
