def main():

    lst = []
    element = str(input("Enter a list of elements separated by spaces: ")).split()
    while element:
        
        lst.append(element)
        element = str(input("Enter an element to add to the list: "))
        
        
    print("The list is: ", lst)
 
if __name__ == '__main__':
    main()