# Written on January 19, 2025
# Getting extra pratice on variables

# Local and Global variables

var1 = "Python"
def func1():
    var1 = "PHP" # local variable
    print("Inside func1() var1= ", var1)

def func2():
    print("Inside func2() var1= ", var1)

func1()
func2()

# Global variable in other functions
def func1():
    global var1
    var1 = "PHP"
    print("In side func1() var1= ", var1)

def func2():
    print("Inside func2() var1= ", var1)

func1()
func2()


############################
# Problem 1: Counter
# Define a global variable to count the number of function calls
global count
count = 1

def increment_count():
    """Increments the global count variable by 1."""
    global count #Explicitly declare that we are using the global variable
    count += 1

# Call the function multiple times
increment_count()
increment_count()
increment_count()

print("Calling this fuction ", count, "times.")

# Global Counter with Nested Functions:
# global count
count = 0

def outer_function():
    def inner_function():
        global count
        count += 1
    inner_function()

outer_function()
print("Count after outer_function call:", count)

outer_function()
print("Count after second outer_function call:", count)


# Global Counter with Class
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

counter = Counter()
counter.increment()
counter.increment()
print("Counting using class:", counter.count)

###
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print(f"A new dog named {self.name} has been created! The breed is a {self.breed}.")

my_dog = Dog("Buddy", "Golder Retriever")


# Global Counter with Decorator
def count_calls(func):
    global count
    count = 0

    def wrapper(*args, **kwargs):
        global count
        count += 1
        return func(*args, **kwargs)
    
    return wrapper

@count_calls
def my_function():
    pass

my_function()
my_function()
print("Function was called", count, "times.")

##
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@counter
def add(x, y):
    return x + y

@counter
def subtract(x, y):
    return x - y

print(f"add was called {add.count} times before being used.") 
print(f"subtract was called {subtract.count} times before being used.")

result1 = add(2, 3)
print(f"add(2, 3) = {result1}")
print(f"add was called {add.count} times after the first call.")

result2 = subtract(5, 2)
print(f"subtract(5, 2) = {result2}")
print(f"subtract was called {subtract.count} times after the first call.") 

print(f"add was called {add.count} times in total.")
print(f"subtract was called {subtract.count} times in total.")

##
def my_function(*args, **kwargs):
    print("args:", args)  # Prints the tuple of positional arguments
    print("kwargs:", kwargs)  # Prints the dictionary of keyword arguments

my_function(1, 2, 3, name="Alice", age=30)


########################
# Problem 2: Modify list
my_list = [1, 2, 3]

def modify_list():
    """Modifies the global list by appending a new value"""
    global my_list
    my_list.append(4)

modify_list()
print("\n Modify list: ", my_list) # Output [1, 2, 3, 4]


###################
# Problem 3: Nested Functions
def outer_function():
    """Defines a nested function that accesses a nonlocal variable."""
    x = "outer"

    def inner_function():
        # Access the nonlocal variable 'x'
        nonlocal x
        x = "inner"
        print("Inner function:", x)

    inner_function()
    print("Outer function:", x)

outer_function()


##################
# Problem 4: Default Argument with Mutable Object
def append_to_list(value, my_list=[]):
    """Appends a value to the list.
    This demonstrates potential pitfalls with mutable default arguments."""
    my_list.append(value)
    return my_list

list1 = append_to_list(10)
list2 = append_to_list(20)

print(list1) # Output: [10, 20]
print(list2) # Output: [10, 20]

# Explanation:
# The default argument 'my_list' is created once and shared
# between all function calls.


######################
# Problem 5: Global Keyword in Nested Functions
global_var = 0

def outer_function():
    def inner_function():
        global global_var
        global_var += 1

    inner_function()

outer_function()
print(global_var) # Output: 1