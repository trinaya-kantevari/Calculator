# Calculator
### Calculator in python for studying unittest

How to use (Example [here](https://github.com/AlfredoFilho/Calculator/blob/main/exampleuse.py)):
```python
from Calculator import Calculator

calc = Calculator()

resultDivision = calc.divide(100, 50) # 2.0
resultMultiplication = calc.multiply(50, 50) # 2500
resultSum = calc.sum(50, 50) # 100
resultSubtraction = calc.subtract(50, 50) # 0
```


For run tests:
```bash
python test_calculator.py -v
```
