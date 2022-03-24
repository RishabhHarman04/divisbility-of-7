import unittest
def check(x):
    if x%7 == 0:
        return True

    else:
        return False

class EvenOrOddApp(unittest.TestCase):

    def test_case_even_check(self):
        x =14
        result = check(x)
        self.assertTrue(result)

    def test_case_odd_check(self):
        x = 15
        result = check(x)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()