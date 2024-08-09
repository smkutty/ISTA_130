import unittest, sys, io
from contextlib import redirect_stdout
from functions import *

class TestFunctions(unittest.TestCase):

    def test_chases(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(chases('dog', 'cat'))
            self.assertEqual('The dog chases the cat\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            chases('lion', 'zebra')
            self.assertEqual('The lion chases the zebra\n', buf.getvalue())
            
    def test_sum3(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(sum3(3, 3, 3))
            self.assertEqual('The sum of the arguments is: 9\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            sum3(10, 5, 1.1)
            self.assertEqual('The sum of the arguments is: 16.1\n', buf.getvalue())
            
    def test_forecast(self):
        random.seed(25)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(forecast())
            self.assertEqual('Chance of rain today: 48 %\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            forecast()
            self.assertEqual('Chance of rain today: 98 %\n', buf.getvalue())
            
    def test_radians(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(radians(0))
            self.assertEqual('The angle in radians is: 0.0\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            radians(208)
            self.assertEqual('The angle in radians is: 3.63\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            radians(57.4)
            self.assertEqual('The angle in radians is: 1.002\n', buf.getvalue())
            
    def test_decimal(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(decimal(3.71))
            self.assertEqual('Decimal part: 0.71\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            decimal(10.371)
            self.assertEqual('Decimal part: 0.371\n', buf.getvalue())
            
    def test_erf_plus_gamma(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            self.assertIsNone(erf_plus_gamma(3))
            self.assertEqual('Result: 3.0\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            erf_plus_gamma(0.75)
            self.assertEqual('Result: 1.937\n', buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            erf_plus_gamma(0.33)
            self.assertEqual('Result: 3.066\n', buf.getvalue())
            
test = unittest.defaultTestLoader.loadTestsFromTestCase(TestFunctions)
results = unittest.TextTestRunner().run(test)
sys.stdout = sys.__stdout__
sys.stdin = sys.__stdin__
print('Correctness score = ', str((results.testsRun - len(results.errors) - len(results.failures)) / results.testsRun * 60) + ' / 60')
