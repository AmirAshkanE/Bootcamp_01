a = int(input("Input a 4 digit number: "))
        
num1 = a // 1000
a %= 1000

num2 = a // 100
a %= 100

num3 = a // 10
num4 = a % 10

print(f"Your number seperated is \n {num1} \n {num2} \n {num3} \n {num4}")

print(f"The sum of the seperated numbers are: {num1 + num2 + num3 + num4}")