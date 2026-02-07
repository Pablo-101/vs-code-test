import operator

print(operator.contains("Souhail", "h"))
print(operator.contains([1, 2, 3, 4, 5], 9))

print()
print("Identity Operators")  # compare memory location of two variables.
print()

num1 = 7
num2 = 7
num3 = 1

ph1 = "hello world"
ph2 = "hello world"

print(num1 is num3)
print(num2 is not num3)
print(ph1 is ph2)
