import matplotlib.pyplot as plt
import math

# The `SequenceAnalyzer` class in Python calculates an approximation of the natural logarithm using a
# series expansion and provides a method to plot the comparison between the approximation series and
# the math function.
class SequenceAnalyzer:
    def __init__(self, x, eps=1e-6, max_iterations=500):
        self.x = x
        self.eps = eps
        self.max_iterations = max_iterations
        self.results = [0.0]
        self.n = 0

    def calculate_ln_approximation(self):
        """
        This Python function calculates an approximation of the natural logarithm of a given input using
        a series expansion.
        """
        result = 0.0
        sign = 1.0
        term = self.x
        n = 0

        while abs(term) > self.eps and n <= self.max_iterations:
            result += term
            self.results.append(result)
            sign *= -1
            n += 1
            term = sign * (self.x ** (n + 1)) / (n + 1) 

        self.n = n + 1 

    def plot_graphs(self):
        """
        The function `plot_graphs` generates a plot comparing an approximation series with a math function
        based on given results and x values.
        """
        x_values = [i for i in range(self.n)] 
        y_values = self.results

        math_values = [math.log(1 + self.x)] * self.n

        plt.plot(x_values[1:], y_values[1:], label="Approximation Series")
        plt.plot(x_values[1:], math_values[1:], label="Math Function")
        plt.xlabel("Number of Terms (n)")
        plt.ylabel("Function Value")
        plt.legend()
        plt.title("Taylor Series Approximation vs Math Function")
        plt.grid(True)
        plt.savefig("plots.png") 
