from task import task

def main():
    """
    The main function calls the task function to count the number of lowercase symbols and digits, then
    prints the counts.
    """
    lowerSymbols, digits = task()
    print(f"Number of lowercase symbols: {lowerSymbols}\nNumber of digits: {digits}")


if __name__ == "__main__":
    while True:
        main()
        if input("Do you want to start again? (y/n)") != "y":
            break