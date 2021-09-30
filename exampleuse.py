from Calculator import Calculator

calc = Calculator()

# print(calc.divide(100, 0)) # Raise exception ZeroDivisionError
# print(calc.divide(50, "50")) # Raise exception TypeError
# print(calc.multiply(50, "50")) # Raise exception TypeError
# print(calc.sum(50, "50")) # Raise exception TypeError
# print(calc.subtract(50, "50")) # Raise exception TypeError

print(calc.divide(100, 50)) # 2.0
print(calc.multiply(50, 50)) # 2500
print(calc.sum(50, 50)) # 100
print(calc.subtract(50, 50)) # 0