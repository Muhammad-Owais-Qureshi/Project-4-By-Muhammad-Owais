def in_range(n, low, high):
  
    if n >= low and n <= high:
      
        return True
   
 

    else:
        return False

def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    if in_range(n, low, high):
        print(f"{n} is in the range [{low}, {high}]")
    else:
        print(f"{n} is not in the range [{low}, {high}]")

if __name__ == '__main__':
    main()

in_range(4, 5, 10)  # True
    
    
    