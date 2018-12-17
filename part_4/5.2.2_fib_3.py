# Remember that Fibonacci's sequence is a sequence of numbers
# where every number is the sum of the previous two numbers.
#
# For this problem, implement Fibonacci recursively, with a
# twist! Imagine that we want to create a new number sequence
# called Fibonacci-3. In Fibonacci-3, each number in the
# sequence is the sum of the previous three numbers. The
# sequence will start with three 1s, so the fourth Fibonacci-3
# number would be 3 (1+1+1), the fifth would be 5 (1+1+3),
# the sixth would be 9 (1+3+5), the seventh would be 17
# (3+5+9), etc.
#
# Name your function fib3, and make sure to use recursion.


# Write your code here!
def fib3(num):
    if num > 3:
        return fib3(num - 1) + fib3(num - 2) + fib3(num - 3)
    else:
        return 1


# The lines below will test your code. If your funciton is
# correct, they will print 1, 3, 17, and 57.
print(fib3(3))
print(fib3(4))
print(fib3(7))
print(fib3(9))
