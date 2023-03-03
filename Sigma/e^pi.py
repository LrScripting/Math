import math

#factorial function with tail recursion
def factorial(n, a=1):
    if n == 1:
        return a
    else:
        return factorial(n-1, n*a)

# helper function to get value of expression each iteration
# takes in n to track number of iterations and x as the value we're subbing into expression
def func(n, x):
  # will return pi**n / pi! for each iteration and accumulate that value
    return (x**n)/ factorial(n)
  
# sigma function, takes in n's start and end value and the function you're applying to n  
def summation(start, stop, func):
    final = 1
    i = start
    while i <= stop:
        final += func(i, math.pi)
        i+=1
    return final


print(summation(1, 50, func))
 
