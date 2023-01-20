a = float(input("Input value for a side: "))
b = float(input("Input value for a side: "))
c = float(input("Input value for a side: "))

p = (a + b + c)
print(str(p) + " cm")
p /= 2
area = (p*(p-a)*(p-b)*(p-c))**0.5
print(str(area) + " cm2")
