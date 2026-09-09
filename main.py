print("Welcome to the Pattern Genrator and Number Analyzer!")
print()

while True:
    print("Select an option :")
    print("1. Generate  a pattern ")
    print("2. Analyze a Range of Number ")
    print ("3.Exit")

    print()
    choice = int(input("Enter your Choice:(1/2/3)"))
    if choice==1:
        num=int(input("Enter the Number of Rows for the Pattern: "))
        print("Pattern")
        for i in range(1,num+1):
            print("*"*i)
        print()
    elif choice == 2:
        start = int(input(" Enter the Start of the Number :"))
        end = int(input("Enter the End of the Number:"))
        total = 0
        print()
        for i in range(start,end + 1):
            
            if i % 2 == 0:
                print(f"Number {i} is Even")
            else:
                print(f" Number {i} is Odd")
            total=total+i
        print(f" Sum of all number is from {start} to {end} is:{total}")

        print()
    elif choice==3:
        print("Exiting the Program .. Goodbye !")
        break
    else:
        print(" invalid choice ") 



