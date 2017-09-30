import unittest

def is_prime(num):
    for elem in range(num):
        if elem !=num and elem % num == 0:
            return False
        else:
            return True

class TestCases(unittest.TestCase):
    def test_is_five_prime(self):
        self.assertFalse(is_prime(5))

if __name__ == "__main__" :
    unittest.main()

print [d['value'] for d in l]
