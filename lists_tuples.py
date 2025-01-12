users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print("Dave" in emptylist)

print(users[0])
print(users[-2])

print(users.index('Sara'))

print(users[0:2]) # this will not include the item of 2nd position
print(users[1:])
print(users[-3:-1])

print(len(data))

# Add items
users.append('Elsa')
print(users)

users += ['Jason'] # Makes sure it has bracket or else it will consider every letter as a value
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

# users.extend(data)
# print(users)

# Insert items to our list
users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)

# Replace items
users[1:3] = ['Robert', 'JPJ']
print(users)

# Remove items
users.remove('Bob')
print(users)

# Remove last item from the list
print(users.pop())
print(users)

# Remove specific user or item from the list
del users[0]
print(users)

#del data
data.clear() #empty the list
print(users)

# Sort data
users[1:2] = ['dave'] # lower case comes after uppercase
users.sort()
print(users)

users.sort(key=str.lower) # Include the lowercase in the correct alphabetical order
print(users)

# Sort in reverse order
nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# Sort in ascending order
# nums.sort()
# print(nums)

# Sort in descending order
# nums.sort(reverse=True)
# print(nums)

# Keep the original list, global sorted function
print(sorted(nums, reverse=True))
print(nums) # Lets check the orginal list

# Make a copy
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

# Check the type of list
print(type(nums))

# Create a new list
mylist = list([1, "Neil", True])
print(mylist)

# Tuples

mytuple = tuple(('Dave', 42, True))
anothertuple = (1, 4, 2, 8)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# Create a new list out of mytuple
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

# Unpack a tuple, putting values in the variables name
# The * (asterick) puts a list in the variable
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2)) # count how many occurences of the number two are inside of anothertuple