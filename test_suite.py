import unittest
from test_module1 import Test1
from test_module2 import Test2


if __name__ == "__main__":
    suite = unittest.TestSuite()  # create test suite

    # hold a collection for all test cases
    suite.addTest(Test1('test_readData'))
    suite.addTest(Test1('test_plot'))
    suite.addTest(Test2('test_readData'))
    suite.addTest(Test2('test_plot'))

    runner = unittest.TextTestRunner()
    runner.run(suite)

