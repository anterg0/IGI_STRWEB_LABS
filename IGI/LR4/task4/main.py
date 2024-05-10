from classes import Rectangle, Pentagon

def input_parameters():
    shape = input("Enter shape (rectangle or pentagon): ")
    if shape == "rectangle":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        color = input("Enter color: ")
        return Rectangle(width, height, color)
    elif shape == "pentagon":
        side_length = float(input("Enter side length: "))
        color = input("Enter color: ")
        return Pentagon(side_length, color)
    else:
        print("Invalid shape input.")
        return None

def main():
    figure = input_parameters()
    print(f'{figure.getName()}')
    if figure:
        print(figure.get_info())

if __name__ == "__main__":
    main()
