import task as modules
import math

def main():
    x = modules.check_x()
    eps = modules.check_x()
    max_iterations = 500

    result, n = modules.ln_approximation(x, eps, max_iterations)
    math_result = math.log(1 + x)
    
    print("\nX\t n\t F(X)\t MathF(X)\t eps")
    print(f"{x}\t {n}\t {result:.6f}\t {math_result:.6f}\t {eps:.6f}")
        
if __name__ == "__main__":
    while True:
        main()
        if input("Do you want to start again? (y/n) ") != 'y':
            break