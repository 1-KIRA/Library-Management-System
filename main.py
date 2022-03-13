#Main python File

#Other three modules are imported for execution along with datetime from Python Standard Library.
import borrow
import dt
import ListSplit
import Returned


while(True):
    print("      Welcome to the library management system   ")
    print("--------------------------------------------------------")
    print("Enter 1. To Display")
    print("Enter 2. To Borrow a Book")
    print("Enter 3. To Return a Book")
    print("Enter 4. To Exit")
    try:
        a = int(input("Select a choice from 1-4: "))
        print()
        if (a == 1):
            #Calling defined function to display all the available books in the Library.
            with open("Books info.txt", "r") as f:
                lines = f.read()
                print(lines)

        elif(a == 2):
             #User input for number of books they want to return and their borrow duration.
            ListSplit.listSplit()
            borrow.borrowBook()
        elif(a == 3):
            ListSplit.listSplit()
            Returned.returnBook()
        elif(a == 4):
            print("Thank you for using the library management system ")
            break
        else:
            print("Please enter a valid choice from 1-4")
    except ValueError:
        print("Please input as suggested.")


