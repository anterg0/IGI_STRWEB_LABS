def check_x():
    """
    This function prompts the user to input a number between 0 and 1.
    It continuously asks for input until a valid number is entered.

    Args:
    No parameters.

    Returns:
    A float value representing the input number if it's within the range [0, 1].

    Raises:
    ValueError: If the input is not a valid float number.
    """
    
    while True:
        try:
            number = float(input("Enter number between 0 and 1: "))
            if 0 <= number < 1:
                return number
            else:
                print("That's not a number between 0 and 1.")
        except ValueError:
            print("Invalid input.")
            
            
            

def ln_approximation(x, eps=1e-6, max_iterations=500):
    """
    Calculates the value of the natural logarithm of 1 + x using the Taylor series expansion.

    Args:
        x (float): the value of x.
        eps (float, optional): the accuracy of the approximation. Defaults to 1e-6.
        max_iterations (int, optional): the maximum number of iterations. Defaults to 500.

    Returns:
        tuple[float, int]: a tuple containing the approximation and the number of terms used in the approximation.

    Raises:
        ValueError: if x is not in the range (-1, 1].

    """

    result = 0.0
    sign = 1.0
    term = x
    n = 1

    while abs(term) > eps and n <= max_iterations:
        result += term
        sign *= -1
        n += 1
        term = sign * (x ** n) / n

    return result, n
