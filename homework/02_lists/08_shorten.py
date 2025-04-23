
MAX_LENGTH : int = 3

def shorten(lst):

    while len(lst) > MAX_LENGTH:
        element = lst.pop()
        print(f"shorten is now: {element}")

def get_list():
    lst = [] 
    elem = input("Enter a list element (or 'done' to finish): ")
    while elem != "":
        lst.append(elem)
        elem = input("Enter a list element (or 'done' to finish): ")
    return lst

     

def main():
    lst = get_list()
    shorten(lst)
   
if __name__ == '__main__':
    main()