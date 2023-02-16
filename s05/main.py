# def sqr_root(n):
#     n = n**0.5
#     return n

# a = input().split()

# for i in a:
#     res = sqr_root(int(i))
#     print(res)

# def tri_draw(n):
#     i=1
#     while i <= n:
#         print("*"*i)
#         i+=1

# n = int(input())
# tri_draw(n)
# from functools import reduce
# a = [1, 2, 3, 4, 5, 6, 7]


# def mult(x, y):
#     return x*y
# # def and_logical(x,y):
# #     return bool(x) and bool(y)


# def new_all(a):
#     return reduce(lambda x, y: bool(x) and bool(y), a)


# def new_any(a):
#     return reduce(lambda x, y: bool(x) or bool(y), a)


# print(reduce(mult, a))
# print(new_all(a))
# print(any(a))


# a = [1, -2, 4, 5, -6, 7]

# print(sorted(a,key= lambda x: abs(x)))

# def add2(a,b,c=0):                          #if user doesnt give any value to c the default is set, so a and b are required and c is optional
#     return a+b+c

# add2(c=2, a=4, b=6)

a= [[1,-2],[5,-6],[4,7]]

print(sorted(a,key= lambda x:sum(x),reverse=True ))