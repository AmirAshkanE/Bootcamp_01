a = int(input("input a digit: "))
b = int(input("input a digit: "))

print(f"a+b = {a+b}, a*b = {a*b}, a-b = {a-b}, a/b = {a/b}, a**b = {a**b}, a//b = {a//b}, a%b = {a%b}")

print(f"a and b = {a and b}, a or b = {a or b}, a & b = {a & b}, a ^ b = {a ^ b}, a | b = {a | b}")

bin_a = bin(a)
bin_b = bin(b)

print(f"binary a '{bin_a}' + binary b '{bin_b}' = {bin(a + b)}")
print(f"binary a '{bin_a}' - binary b '{bin_b}' = {bin(a - b)}")
print(f"binary a '{bin_a}' * binary b '{bin_b}' = {bin(a * b)}")
print(f"binary a '{bin_a}' // binary b '{bin_b}' = {bin(a // b)}")
print(f"binary a '{bin_a}' % binary b '{bin_b}' = {bin(a % b)}")
print(f"binary a '{bin_a}' ** binary b '{bin_b}' = {bin(a ** b)}")

oct_a = oct(a)
oct_b = oct(b)

print(f"oct a '{oct_a}' + oct b '{oct_b}' = {oct(a + b)}")
print(f"oct a '{oct_a}' - oct b '{oct_b}' = {oct(a - b)}")
print(f"oct a '{oct_a}' * oct b '{oct_b}' = {oct(a * b)}")
print(f"oct a '{oct_a}' // oct b '{oct_b}' = {oct(a // b)}")
print(f"oct a '{oct_a}' % oct b '{oct_b}' = {oct(a % b)}")
print(f"oct a '{oct_a}' ** oct b '{oct_b}' = {oct(a ** b)}")

hex_a = hex(a)
hex_b = hex(b)

print(f"hex a '{hex_a}' + hex b '{hex_b}' = {hex(a + b)}")
print(f"hex a '{hex_a}' - hex b '{hex_b}' = {hex(a - b)}")
print(f"hex a '{hex_a}' * hex b '{hex_b}' = {hex(a * b)}")
print(f"hex a '{hex_a}' // hex b '{hex_b}' = {hex(a // b)}")
print(f"hex a '{hex_a}' % hex b '{hex_b}' = {hex(a % b)}")
print(f"hex a '{hex_a}' ** hex b '{hex_b}' = {hex(a ** b)}")