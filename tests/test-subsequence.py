#!/usr/bin/env python
import os, sys
import unittest
import xmlrunner
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from subsequence import is_subsequence
import random
import string

class TestSubsequence(unittest.TestCase):
    def test_empty_s(self):
        for i in range(100):
            n = random.randint(0,1000)
            text = ''.join(random.choices(string.ascii_lowercase,k=n))
            self.assertTrue(is_subsequence('',text))
    def test_empty_t(self):
        for i in range(100):
            n = random.randint(1,1000)
            sub = ''.join(random.choices(string.ascii_lowercase,k=n))
            self.assertFalse(is_subsequence(sub,''))
    def test_s_gt_t(self):
        for i in range(100):
            n = random.randint(1,1000)
            m = random.randint(1,1000)
            if n > m:
                sub = ''.join(random.choices(string.ascii_lowercase,k=n))
            elif n == m:
                sub = ''.join(random.choices(string.ascii_lowercase,k=n-1))
            else:
                sub = ''.join(random.choices(string.ascii_lowercase,k=m))
            text = ''.join(random.choices(string.ascii_lowercase,k=n))
            self.assertFalse(is_subsequence(sub,text))
    def test_basic_true(self):
        self.assertTrue(is_subsequence("a","a"))
        self.assertTrue(is_subsequence("asdf","asdf"))
        self.assertTrue(is_subsequence("asdf","asdfffffffffffff"))
        self.assertTrue(is_subsequence("asdf","aaaaaaaaaaaaaaasdfffffffffffff"))

        for i in range(100):
            n = random.randint(1,100)
            sub = ''.join(random.choices(string.ascii_lowercase,k=n))
            text = ""
            for c in sub:
                letters = ""
                for k in range(random.randint(0,100)):
                    letters+=random.choice(string.ascii_lowercase)
                text += c + letters
            self.assertTrue(is_subsequence(sub,text))
    def test_basic_false(self):
        self.assertFalse(is_subsequence("a","d"))
        self.assertFalse(is_subsequence("asd","dsa"))
        self.assertFalse(is_subsequence("aaaaaaaaa","dddddddddddddd"))
    # def test_wrong(self):
    #     self.assertTrue(is_subsequence("a","b"))
def runner(output='python_tests_xml'):
    return xmlrunner.XMLTestRunner(output=output)
def find_tests():
    # return unittest.TestLoader().discover('TestSubsequence')
    return unittest.TestLoader().loadTestsFromTestCase(TestSubsequence)
if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestSubsequence)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    runner().run(find_tests())
