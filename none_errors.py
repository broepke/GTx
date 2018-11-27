# I think there is a problem with this "problem"
# Interlude 3.4.2: Functions Returning None

def some_function_1(i, j):
    print(i + j)

result1 = some_function_1(5, 6)

def some_function_2(i, j):
    return i + j

result2 = some_function_2(5, 6)

def some_function_3(i, j, k):
    product = i * j
    sum = j + k
    metaproduct = product * sum

result3 = some_function_3(1, -1, 5)


def some_function_4(strokes, par):
    score = strokes - par
    print("Your score is", score)
    return score

result4 = some_function_4(5, 4)

def some_function_5(total, tax):
    print("Your total is", total * tax)
    return None

result5 = some_function_5(15.99, 1.08)

def some_function_6(i):
    the_square = i ** 2
    return the_square
    return None

result6 = some_function_6(5)

def some_function_7(j):
    the_cube = i ** 3
    return None
    return the_cube

# i vs j in the input parameter
# result7 = some_function_7(5)


def some_function_8(l, w, h):
    return print(l * w * h)

# doesn't call anything
# result8  = some_function(2, 2, 4)


print("1", result1)
print("2", result2)
print("3", result3)
print("4", result4)
print("5", result5)
print("6", result6)
print("Error")
print("Error")