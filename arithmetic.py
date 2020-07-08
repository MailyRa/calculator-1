"""Functions for common math operations."""
def add(num1, num2):
    """Return the sum of the two inputs."""
    total = num1 + num2
    return total

print("Here is the answer of addition: {}".format(add(2,2)))

def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    total = num1 - num2
    return total 

print("Here is the answer of subtraction: {}".format(subtract(4,2)))



def multiply(num1, num2):
    """Multiply the two inputs together."""
    total = num1 * num2
    return total

print("Here is the answer of multiplication: {}".format(multiply(2,2)))


def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    total = num1/num2
    return total 

print("Here is the answer of dividision: {}".format(divide(2,2)))

def square(num1):
    """Return the square of the input."""
    total =  2 ** (num1)
    return total
print("Here is the answer of square: {}".format(square(2)))

def cube(num1):
    """Return the cube of the input."""
    total = 3 ** (num1)
    return total 
print("Here is the answer of cube: {}".format(cube(2)))

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    total = pow(num1, num2)
    return total 
print("Here is the answer of power: {}".format(power(2,2)))

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    total = num1 % num2
    return total 
print("Here is the answer of mod: {}".format(mod(2,2)))
