# Create a list colors = ["red", "blue"]. Add "green", remove "red".

def modify_color_list() -> None:
    colors = ["red", "blue"]
    colors.append("green")
    colors.remove("red")
    for color in colors:
        print(color)

def main() -> None:
    modify_color_list()

if __name__ == "__main__":
    main()