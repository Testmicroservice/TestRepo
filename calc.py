import time
import pprint

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b, a % b 

def sub(a, b):
    return a - b

def square(a):
    return a * a

num1 = 5
num2 = 7

sum = add(num1, num2)
time.sleep(5)
print("Sum = ", sum)

prod = mult(num1, num2)
print("Product = ", prod)

quot = div(num1, num2)
print("Quotient, Remainder = ", quot)

diff = sub(num1, num2)
print("Difference = ", diff)

sqr = square(num1)
print("Sqare = ", sqr)
