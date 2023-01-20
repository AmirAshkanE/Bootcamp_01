num = int(input("input a 5 digit number: "))

num1 = num // 10000
num %= 10000

num2 = num // 1000
num %= 1000

num3 = num // 100
num %= 100

num4 = num // 10
num5 = num % 10

print(f"your number is {num1}, {num2}, {num3}, {num4}, {num5}")