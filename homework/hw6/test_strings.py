import unittest, io, inspect, os
from contextlib import redirect_stdout
from strings import *

'''
Files needed:
redact_in.txt, highlight_in.txt, plagiarism_in.txt
'''

class TestStrings(unittest.TestCase):
    def test_US_to_EU(self):
        self.assertEqual('12.3.18', US_to_EU('3/12/18'))
        self.assertEqual('11.12.2018', US_to_EU('12/11/2018'))
        self.assertEqual('1.2.3', US_to_EU('2/1/3'))
        
    def test_is_phone_num(self):
        self.assertTrue(is_phone_num('123-456-7890'))
        self.assertFalse(is_phone_num('123-456'))
        self.assertFalse(is_phone_num('123-456-789O'))
        self.assertFalse(is_phone_num('123-456-78911'))
        self.assertFalse(is_phone_num('1123-456-7891'))
        self.assertFalse(is_phone_num('123-456-7891-'))
        self.assertFalse(is_phone_num('1d3-456-7891'))
        self.assertFalse(is_phone_num('1234456-7891'))
        self.assertFalse(is_phone_num('123-4S6-7891'))
        self.assertFalse(is_phone_num('(123)-456-7891'))
        self.assertFalse(is_phone_num('(123)456-7891'))
        
    def test_redact_line(self):
        self.assertEqual('XXX-XXX-XXXX\n', redact_line('123-456-7890\n'))
        self.assertEqual('XXX-XXX-XXXX 123-456-78901\n', 
             redact_line('123-456-7890 123-456-78901\n'))
        self.assertEqual('XXX-XXX-XXXX  123-456-78901   XXX-XXX-XXXX\n', 
             redact_line('123-456-7890  123-456-78901   123-456-7890\n'))
        self.assertEqual('XXX-XXX-XXXX XXX-XXX-XXXX XXX-XXX-XXXX\n', 
             redact_line('123-456-7890 333-456-7890 123-456-7890\n'))
        self.assertEqual('XXX-XXX-XXXX blah XXX-XXX-XXXX blah blah XXX-XXX-XXXX\n', 
             redact_line('123-456-7890 blah 333-456-7890 blah blah 123-456-7890\n'))
        self.assertEqual('123-456-78901\n', redact_line('123-456-78901\n'))
        
    def test_redact_file(self):
        if 'redact_in_redacted.txt' in os.listdir():
            os.remove('redact_in_redacted.txt')
        correct = ('XXX-XXX-XXXX\nXXX-XXX-XXXX 123-456-78901\n' +
            'XXX-XXX-XXXX 123-456-78901 XXX-XXX-XXXX\n' +
            'XXX-XXX-XXXX XXX-XXX-XXXX XXX-XXX-XXXX\n' +
            'XXX-XXX-XXXX blah XXX-XXX-XXXX blah blah XXX-XXX-XXXX\n' +
            '123-456-78901\n')
        redact_file('redact_in.txt')
        self.assertEqual(correct, open('redact_in_redacted.txt').read())
        self.assertTrue('close' in inspect.getsource(redact_file))

    def test_plagiarism(self):
        self.assertFalse(plagiarism('highlight_in.txt', 'redact_in.txt'))
        self.assertTrue(plagiarism('highlight_in.txt', 'plagiarism_in.txt'))
        self.assertTrue(plagiarism('plagiarism_in.txt', 'highlight_in.txt'))
        self.assertTrue(plagiarism('plagiarism_in.txt', 'redact_in.txt'))
        self.assertTrue('close' in inspect.getsource(plagiarism))
        
    def test_count_word(self):
        self.assertEqual(8, count_word('highlight_in.txt', 'Rocket'))
        self.assertEqual(1, count_word('highlight_in.txt', 'say'))
        self.assertEqual(0, count_word('redact_in.txt', 'Rocket'))
        self.assertEqual(11, count_word('redact_in.txt', '123'))
        self.assertEqual(13, count_word('redact_in.txt', '456'))
      
        
test = unittest.defaultTestLoader.loadTestsFromTestCase(TestStrings)
results = unittest.TextTestRunner().run(test)
#sys.stdout = sys.__stdout__
#sys.stdin = sys.__stdin__
print('Correctness score = ', str((results.testsRun - len(results.errors) - len(results.failures)) / results.testsRun * 100) + '%')
