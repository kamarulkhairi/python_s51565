def add_numbers(a, b):
    return a + b


def print_arguments(augmented_add_number1, augmented_add_number2):
    print("Arguments are: ", augmented_add_number1, augmented_add_number2, " and will return ",
          2 * (add_numbers(augmented_add_number1, augmented_add_number2)))
    return 2 * (add_numbers(augmented_add_number1, augmented_add_number2))


augmented_add_numbers_a = int(input("Enter your numbers"))
augmented_add_numbers_b = int(input("Enter your numbers"))
print_arguments(augmented_add_numbers_a, augmented_add_numbers_b)
