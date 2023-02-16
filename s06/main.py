# while True:
#     a=float(input("a: "))
#     b=float(input("b: "))
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print("something went wrong!")
#     except FileExistsError:
#         print("Incorrect file")

# ----------------------------------------------------------------------------------------------------------


# def new_add (a,b,c=None):
#     if c is None:
#         return a+b
#     else:
#         return (a+b)*c
# This is Funciton overloading

# def sample_def (a,*arg,key,**kwarg):                      # using *arg(arg and kwarg are naming conventions) arg is a tuple parameter that can take as many arguments as we want **kwarg for keyword argument a dictionary type
#     print(type(arg))
#     print(type(kwarg))
#     print(kwarg)
#     if len(arg) == 1:
#         print(1)
#     elif len(arg)==2:
#         print(2)
#     elif len(arg) > 2:
#         raise Exception("Sample_def can only run with <= 2 arguments")                          # we use raise to create our own exceptions


# pa= [2,3,4]
# keyword_args={"age":20,"gender":"male"}
# sample_def(10,*pa,name="Ashkan")
# sample_def(10,2,3,4,name="Ashkan")
# sample_def(*pa,**keyword_args)


# def def1(x):
#     x+=1
#     print(x)
    
# a=2
# def1(a)
# # this is calling by value
# print(a)

# def def2(x):
#     x.append(10)
#     print(x)
    
# a=[2]
# def2(a)
# # this is calling by reference
# print(a)


# *DECORATORS*

# def sample_decorator(input_def):

    
    
#     return wraper_def


from time import time

# def loop():
#     x=0
#     for i in range(1,10000000):
#         x+=1/i
#     print(x)

def loop2():
    x=0
    for i in range(1,10000000):
        x+=1/(i**0.5)
    print(x)
    
# star_time = time()
# loop()
# end_time = time()
# print(end_time-star_time)


def time_decorator(f):
    def wrapper():
        star_time = time()
        f()
        end_time=time()
        print(end_time-star_time)
    return wrapper

@time_decorator
def loop():
    x=0
    for i in range(1,10000000):
        x+=1/i
    print(x)

loop = time_decorator(loop)
