def get_name(name: str):
    return name

# There is no need to edit code beyond this point

def main():
    userName = input("What is your name? ") # input() will return a string which we store to the 'userName' variable here
    name = get_name(userName) # get_name() will return a string which we store to the 'name' variable here
    print("Howdy", name, "! 🤠")

if __name__ == '__main__':
    main()