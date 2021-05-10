import coffeeshop as c

def runProgram():
    print("\n")
    print("Welcome to the Coffee Shop Database Application!")
    print("This is a one stop shop for Chapman students to find and keep track of all of the Coffee Shops in Orange County.")
    print("\n")
    print("---------------------------------------------------------------------------------")
    userInput = ""
    status = False
    while (status == False):
        c.printMenu()
        print("---------------------------------------------------------------------------------")
        userInput = input("What would you like to do? Enter the numerical value: ")
        print("\n")
        if (userInput == "1"):
            print("Here is a display all current information in the coffee shop database: ")
            c.displayRecords()
        elif (userInput == "2"):
            print("You chose to print out filtered results!")
            c.parameterQueries()
        elif (userInput == "3"):
            print("You chose to add a new OC coffee shop to the database!")
            c.createNewRecord()
        elif (userInput == "4"):
            print("You chose to print out filtered results!")
            c.deleteRecord()
        elif (userInput == "5"):
            c.updateRecord()
        elif (userInput == "6"):
            c.updateDrink()
        elif (userInput == "7"):
            c.updateFood()
        elif (userInput == "8"):
            c.updateEmployee()
        elif (userInput == "9"):
            c.addFood()
        elif (userInput == "10"):
            c.addDrink()
        elif (userInput == "11"):
            c.addEmployee()
        elif (userInput == "12"):
            c.generateReports()
        elif (userInput == "13"):
            print("Exiting program. Thank you!")
            print("---------------------------------------------------------------------------------")
            status = True
        else:
            print("Input invalid. Please enter a number between 1 and 6. ")
            continue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runProgram()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
