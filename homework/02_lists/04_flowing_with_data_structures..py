def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)

  
def main():
    bold_italic = '\033[1;3m'
    user = input(f"{bold_italic}Enter your massage: ")
    my_list = []
    print(f"List Before: {user}")
    add_three_copies(my_list, user)
    print(f"List After: {my_list}")


if __name__ == "__main__":
    main()