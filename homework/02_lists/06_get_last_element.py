def get_last_element(lst):

    print(lst[-1])  


def get_list():

    lst = []
    elem = str(input("Enter the name of elements in the list: "))
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_list()
    get_last_element(lst)


if __name__ == '__main__':
    main()    