from task import func1, func2, func3

def main():
    """
    The main function calls three other functions to retrieve words with odd lengths, the shortest word
    starting with 'i', and duplicate words, and then prints out the results.
    """
    odd = func1()
    iWord = func2()
    duplicate = func3()
    print("Words with odd length:")
    for key in odd:
        print(key)
    print("\nShortest word starting with 'i':", iWord)
    print("\nDuplicate words:", duplicate)

if __name__ == "__main__":
    while True:
        main()
        if input("Do you want to start again? (y/n)") != "y":
            break