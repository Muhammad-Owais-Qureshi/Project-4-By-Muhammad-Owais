def multiple_print(massage:str, repeat:int):
    for i in range(repeat):
        print(massage)



def main():
    massage = input("Enter a message: ")
    repeat = int(input("Enter a number: "))
    multiple_print(massage, repeat)
    
    
if __name__ == '__main__':
    main()
   

