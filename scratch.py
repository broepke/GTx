my_list = [["a", 2], ["b", 1]]


def takeSecond(elem):
    return elem[1]

my_list.sort(key=takeSecond)

print(my_list)