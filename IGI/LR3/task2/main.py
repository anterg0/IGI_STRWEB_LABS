from input import func,auto_func,gen

def main():
    """
    The main function prompts the user to choose between manual or generator input, generates numbers
    based on the choice, and calculates the minimum number among them.
    """
    while True:
        choice = input("Use manual or generator input? (manual/generator) ")
        result = 0
        if choice == "manual":
            result = func()
        elif choice == "generator":
            inputFlag = True
            n = 0
            while inputFlag:
                n = input("How many numbers are needed to be generated? ")
                if not int(n):
                    print("Invalid input.")
                else:
                    inputFlag = False
            result = auto_func(gen(int(n)))
        print(f"Min number is: {result}")
        break

if __name__ == "__main__":
    while True:
        main()
        if input("Do you want to start again? (y/n) ").lower() != 'y':
            break
