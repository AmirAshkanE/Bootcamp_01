n =int(input())
m =int(input())
s=0

for i in range(-10,m+1):
    for j in range(1,n+1):
        s += int(((i+j)**3)/j**2)
        

print(s)        