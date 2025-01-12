def hello_world(): # definition of a funtion
    print("Hello world!")

hello_world() # call the function hello()

# parameter
def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

total = sum()
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave", "John", "Sara")

# kwargs = key word arguments
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Dave", last = "Gray")