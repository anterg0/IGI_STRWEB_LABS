def dec_func(func):
    def foo():
        print("It's time to input the string.")
        n1 = func()
        print(f"These are the results: {n1}")
        return n1
    return foo


@dec_func
def task():
    """
    The function `task` counts the number of lowercase letters and digits in a given input string.
    :return: The `task` function is returning a tuple containing two values: the count of lowercase
    letters (excluding spaces) in the input string and the count of digits in the input string.
    """
    string = list(input("Input string: "))
    lowerSymCount = 0
    digitsCount = 0
    for symbol in string:
        if symbol.islower() and symbol != " ":
            lowerSymCount += 1
        elif symbol.isdigit():
            digitsCount += 1
    return lowerSymCount, digitsCount