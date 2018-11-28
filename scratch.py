try:
    print(int("a" + 1 + "a"))
except TypeError as error:
    print(error)