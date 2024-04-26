def fill_list(float_list):
    """
    The function `fill_list` takes user input of floats separated by spaces until the user enters '1',
    then converts the input into a list of floats and returns it.
    
    :return: The function `fill_list` returns a list of floats entered by the user.
    """
    while True:
        nums = input("Enter a single or multiple floats separated by space (type 1 to end the input): ")
        num_list = nums.split()
        size = len(num_list)
        if nums == "1":
            break
        if size > 1:
            for i in range(0, size):
                if num_list[i] == '1':
                    break
                if is_float(num_list[i]):
                    float_list.append(float(num_list[i]))
                    print(f"Added {num_list[i]} to the list")
                else:
                    print(f"Invalid input: {num_list[i]} is not a valid float.")
        elif size == 1:
            if is_float(num_list[0]):
                float_list.append(float(num_list[0]))
                print(f"Added {num_list[0]} to the list")
            else:
                print(f"Invalid input: {num_list[0]} is not a valid float.")
    return float_list

def is_float(value):
    """
    Checks if a given value can be converted to a float.
    
    :param value: The value to be checked.
    :return: True if the value can be converted to a float, False otherwise.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

def print_list(float_list):
    """
    The function `print_list` prints the elements of the given list.
    
    :param float_list: The list of floats to be printed.
    """
    if not float_list:
        print("List is empty")
    else:
        for item in float_list:
            print(item)
