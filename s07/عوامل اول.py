n = int(input())

factor = []
output = ""


def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


while n > 1:
    for i in range(2, n+1):
        counter = 0
        while n % i == 0:
            n = n//i
            counter += 1
        if counter > 1:
            output += f"{i}^{counter}*"
        elif counter == 1:
            output += f"{i}*"
print(output[:-1])
