b1 = True
b2 = False
b3 = True

print(b1 and b2 and b3)  # e
print(b1 or b2 or b3)  # ou
print(b1 != b2)  # xor
print(not b1)  # não
print(not b2)  # não
print(b1 and not b2 and b3)  # e não, e

x = 3
y = 4

print(b1 and not b2 and x < y)  # b1 e não b2 e x menor que y
