x1 = float(input("input x1: "))
y1 = float(input("input y1: "))
x2 = float(input("input x2: "))
y2 = float(input("input y2: "))

destination = ((y2 ** 2-y1 ** 2) + (x2**2-x1**2))**0.5

print("Distance is: " + str(destination))
