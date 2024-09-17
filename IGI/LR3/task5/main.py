from input import print_list, fill_list
from task import task

def main():
    """
    The main function allows the user to input a list of floats, print the list, and execute a task
    based on user choice.
    :return: In the `main()` function, when the user selects option 3 to execute the task, `return None`
    is being used to exit the function. This means that the function will return `None` when the task is
    completed.
    """
    float_list = []
    while True:
        choice = input("1. Enter float list\n2. Print the list\n3. Execute the task\n")
        if choice == '1':
            float_list = fill_list(float_list)
        elif choice == '2':
            print_list(float_list)
        elif choice == '3':
            task(float_list)
            return None
        else:
            print("Wrong choice")
            continue

if __name__ == "__main__":
    while True:
        main()
        if input("Do you want to start again? (y/n) ").lower() != "y":
            break
