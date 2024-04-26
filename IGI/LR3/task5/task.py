def task(float_list):
    """
    The function takes a list of numbers, finds the maximum absolute value, and calculates the sum of
    all elements excluding the largest negative number if present.
    
    :param float_list: The list of floats on which the task is performed.
    """
    new_list = [abs(num) for num in float_list]
    print(f"Max absolute float in the list: {max(new_list)}")
    lastPosIndex = len(float_list) - 1
    summa = 0
    if max(float_list) < 0:
        print(f"Sum of all elements before the last positive: {sum(float_list)}")
    else:
        for i in range(len(float_list) - 1, -1, -1):
            if float_list[i] > 0:
                lastPosIndex = i
                break
        for i in range(0, lastPosIndex + 1):
            summa += float_list[i]
        print(f"Sum of all elements before the last positive: {summa}")
    # sorted_list = sorted(float_list)
    # popped_float = sorted_list.pop()
    # if popped_float < 0:
    #     sum_result = sum(sorted_list) + popped_float
    #     print(f"Sum of elements is: {sum_result}")
    # else:
    #     sum_result = sum(sorted_list)
    #     print(f"Sum of elements is: {sum_result}")
