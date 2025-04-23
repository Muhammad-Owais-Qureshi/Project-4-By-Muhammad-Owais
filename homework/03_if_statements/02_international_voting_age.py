CHILD_AGE : int = 16
YOUNG_AGE : int = 25
ADULT_AGE : int = 48

def main():
    # Get the user's age
    user_age = int(input("How old are you? "))
   

   
    if user_age <= CHILD_AGE:
        print("You can vote in young where the voting age is " + str(YOUNG_AGE) + ".")
    
    if user_age >= YOUNG_AGE:
        print("You can vote in young where the voting age is " + str(YOUNG_AGE) + ".")
   
    if user_age >= ADULT_AGE:
        print("You can vote in adult where the voting age is " + str(ADULT_AGE) + ".")

    else:
        print("You cannot vote in child where the voting age is " + str(YOUNG_AGE) + ".")




if __name__ == '__main__':
    main()