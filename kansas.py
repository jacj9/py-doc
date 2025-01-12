from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"


def randomfunfact():
    funfacts = [
        "The capital city is Topeka",
        "State bird is Western Meadowlark",
        "State flower is Sunflower",
        "Song of the state is Home on the Range"
    ]

    index = choice("0123")

    print(funfacts[int(index)])


if __name__ == "__main__":
    randomfunfact()