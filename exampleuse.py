from Calculator import Calculator

calc = Calculator()

# resultDivision = calc.divide(100, 0) # Raise exception ZeroDivisionError
# resultMultiplication = calc.divide(50, "50") # Raise exception TypeError
# resultSum = calc.multiply(50, "50") # Raise exception TypeError
# resultSum = calc.sum(50, "50") # Raise exception TypeError
# resultSubtraction = calc.subtract(50, "50") # Raise exception TypeError

resultDivision = calc.divide(100, 50) # 2.0
resultMultiplication = calc.multiply(50, 50) # 2500
resultSum = calc.sum(50, 50) # 100
resultSubtraction = calc.subtract(50, 50) # 0