# this is a test file use for z_test_unittest.py

def calculate(price, tax=0, discount=0):
    return round((price - discount) * (1 + tax), 2)
