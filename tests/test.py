import pytest
import random

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_addition_positive_test(self):
        a, b = random.uniform(-1e6, 1e6), random.uniform(-1e6, 1e6)

    def test_subtraction_positive_test(self):
        a, b = random.uniform(-1e6, 1e6), random.uniform(-1e6, 1e6)
        assert self.calc.subtraction(self, a, b) == a - b

    def test_multiplication_positive_test(self):
        a, b = random.uniform(-1e6, 1e6), random.uniform(-1e6, 1e6)
        assert self.calc.multiplication(self, a, b) == a * b

    def test_division_positive_test(self):
        a, b = random.uniform(-1e6, 1e6), random.uniform(-1e6, 1e6)
        if b == 0: b = random.randint(-1000, 1000)
        assert self.calc.division(self, a, b) == a / b

    '''def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)'''

    def teardown(self):
        print("Executing the Teardown method")
