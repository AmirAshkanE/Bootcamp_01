# def factorial(n):                       # recursive function
#     if n == 0:
#         return 1
#     else:
#         n_1 = factorial(n-1)
#         return n*n_1

# print(factorial(20))

# from pathlib import Path

# data_address = Path("s07\data.txt")
# f = open(data_address,"r")
# output = f.read()
# print(output)
# # print(dir(data_address.parent))
# print(data_address.parent.resolve())


# for file in data_address.parent.iterdir():
#     print(file)

# from pathlib import Path

# data_address = Path("s07\data.txt")

# f = open(data_address, "w")
# f.write("new data")

# f.close()

# # or

# with open("s07\data.txt","r") as f:
#     print(f)
# doesnt need to be closed does it automatically when thr program is closed

# from pathlib import Path

# data_address = Path("s07\data.txt")
# data_list=[]
# with open(data_address,"r") as f:
#     for line in f:                      # f.readlines() is executed by default f.readline() // reads only the characters in one line
#         temp_list=[]
#         temp_list.append(line)
#         data_list.append(temp_list)
# print(data_list)

# import csv

# with open("s07\data.csv") as f:
#     data = csv.reader(f)                            # csv.reader() is an iterator
#     head = next(data)
#     print(data)
#     print(type(data))
#     for row in data:
#         print(row)
import sys

i=100000
a=list(range(i))
b=range(i)

print(sys.getsizeof(a))
print(sys.getsizeof(b))