name = "Dave" # global scope
count = 1



def another():
    color = "blue" # local scope
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")

another()