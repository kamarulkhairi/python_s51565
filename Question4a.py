def multiply_by_two(x):
    return x * 2


def print_arguments(function):
    print("Arguments are: ", function, " and will return ", multiply_by_two(function))
    return multiply_by_two(function)


insert = int(input('insert numb'))
print_arguments(function=insert)
