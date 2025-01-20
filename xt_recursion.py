""" Recursion exercises from Gemini. Recursion happens when a function calls itself.
Written on: January 19, 2025"""

# 1. Factorial
# Calculate the factorial of a non-negative integer.
# The factorial of a non-negative integer 'n', denoted by 'n!', is the product of all positive integers less than or equal to 'n'.   
# For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.

def factorial(n):
  """
  Calculates the factorial of a non-negative integer.

  Args:
    n: The non-negative integer.

  Returns:
    The factorial of n.
  """
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

# Example usage
result = factorial(5)
print(f"Factorial of 5: {result}")  # Output: Factorial of 5: 120


###########
# 2. Fibonacci Sequence
# Generate the 'n'-th number in the Fibonacci sequence.
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.   
# The sequence typically starts from 0 and 1.

def fibonacci(n):
  """
  Calculates the n-th Fibonacci number.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The n-th Fibonacci number.
  """
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Example usage
result = fibonacci(6)
print(f"6th Fibonacci number: {result}")  # Output: 6th Fibonacci number: 8


#############
# 3. Greatest Common Divisor (GCD)
# Find the greatest common divisor (GCD) of two non-negative integers.

def gcd(a, b):
  """
  Calculates the greatest common divisor of two integers using the Euclidean algorithm.

  Args:
    a: The first integer.
    b: The second integer.

  Returns:
    The greatest common divisor of a and b.
  """
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

# Example usage
result = gcd(48, 18)
print(f"GCD of 48 and 18: {result}")  # Output: GCD of 48 and 18: 6


#########
# 4. Tower of Hanoi
# Solve the classic Tower of Hanoi puzzle.
# The goal is to move all the disks from the source peg to the destination peg, obeying the following rules:
# Only one disk can be moved at a time.
# A larger disk cannot be placed on top of a smaller disk.

def tower_of_hanoi(n, source, auxiliary, destination):
  """
  Solves the Tower of Hanoi puzzle.

  Args:
    n: The number of disks.
    source: The source peg.
    auxiliary: The auxiliary peg.
    destination: The destination peg.
  """
  if n == 1:
    print(f"Move disk 1 from {source} to {destination}")
    return
  tower_of_hanoi(n-1, source, destination, auxiliary)
  print(f"Move disk {n} from {source} to {destination}")
  tower_of_hanoi(n-1, auxiliary, source, destination)

# Example usage
tower_of_hanoi(3, 'A', 'B', 'C')