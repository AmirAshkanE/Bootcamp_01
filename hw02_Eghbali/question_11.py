num = input()

nums = []

for i in num:
    nums.append(i)

reverse_nums = nums[:]

reverse_nums.reverse()

if reverse_nums == nums :
    print("YES")
else:
    print("NO")