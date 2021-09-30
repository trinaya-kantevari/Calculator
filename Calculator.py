from typing import Union


class Calculator:

    def __init__(self):
        '''Calculator class initialiazed'''
        pass

    def divide(self, number1: Union[int, float], number2: Union[int, float]):
        '''
        Parameter:
            number1 (int or float): First number to division
            number2 (int or float): Second number to division

        Returns:
            Float: Returns a division of two numbers informed
        '''

        self.number1 = number1
        self.number2 = number2

        try:
            self.result = self.number1 / self.number2

        except TypeError:
            raise TypeError

        except ZeroDivisionError:
            raise ZeroDivisionError

        return self.result

    def multiply(self, number1: Union[int, float], number2: Union[int, float]):
        '''
        Parameter:
            number1 (int or float): First number to multiplication
            number2 (int or float): Second number to multiplication

        Returns:
            Float or Int: Returns a multiplication of two numbers informed
        '''

        self.number1 = number1
        self.number2 = number2

        if isinstance(self.number1, str) or isinstance(self.number2, str):
            raise TypeError

        self.result = self.number1 * self.number2
        return self.result

    def sum(self, number1: Union[int, float], number2: Union[int, float]):
        '''
        Parameter:
            number1 (int or float): First number to sum
            number2 (int or float): Second number to sum

        Returns:
            Float or Int: Returns a sum of two numbers informed
        '''

        self.number1 = number1
        self.number2 = number2

        try:
            self.result = self.number1 + self.number2

        except TypeError:
            raise TypeError

        return self.result

    def subtract(self, number1: Union[int, float], number2: Union[int, float]):
        '''
        Parameter:
            number1 (int or float): First number to subtraction
            number2 (int or float): Second number to subtraction

        Returns:
            Float or Int: Returns a subtraction of two numbers informed
        '''

        self.number1 = number1
        self.number2 = number2

        try:
            self.result = self.number1 - self.number2

        except TypeError:
            raise TypeError

        return self.result