import math
from classes import SequenceAnalyzer

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

def main():
    x = check_x()
    eps = 1e-6
    max_iterations = 500

    analyzer = SequenceAnalyzer(x, eps, max_iterations)
    analyzer.calculate_ln_approximation()
    analyzer.plot_graphs()

    math_result = math.log(1 + x)
    
    print("\nX\t n\t F(X)\t MathF(X)\t eps")
    print(f"{x}\t {analyzer.n}\t {analyzer.results[-1]:.6f}\t {math_result:.6f}\t {eps:.6f}")

    print("Plot saved successfully.")

if __name__ == "__main__":
    main()
