from DSA.Factorial import Factorial

def testFactorial():
    solution = Factorial()

# test case I: factorial(8) = 40320
    assert solution.factorials(8) == 40320

#test case II: factorial(0) = 1
    assert solution.factorials(0) == 1