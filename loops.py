value = 1
# while value <= 10:
#    print(value)
#    if value == 5:
#       break # stops the loop when reach if statement
#    value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is not equal to " + str(value))

names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue
#     print(x)

# Ranges
# for x in range(4):
#     print(x)

# for x in range(2,4): # starts at 2, stops at 4, but 4 is not included
#     print(x)

for x in range(5,100,5): # increment by 5
    print(x)
else:
    print("Glad that\'s over!")

# Nested Loops

names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")