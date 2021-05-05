import coffeeshop as c

def runProgram():
    print("\n")
    print("Welcome to the Coffee Shop Database Application!")
    print("This is a one stop shop for Chapman students to find and keep track of all of the Coffee Shops in Orange County.")
    print("\n")
    print("---------------------------------------------------------------------------------")
    userInput = ""
    while (userInput != "7"):
        c.printMenu()
        print("---------------------------------------------------------------------------------")
        userInput = input("What would you like to do? Enter the numerical value: ")
        if (userInput == "1"):
            c.displayRecords()
        elif (userInput == "2"):
            c.parameterQueries()
        elif (userInput == "3"):
            c.createNewRecord()
        elif (userInput == "4"):
            c.deleteRecord()
        elif (userInput == "5"):
            c.updateRecord()
        elif (userInput == "6"):
            c.addFood()
        elif (userInput == "7"):
            c.addDrink()
        elif (userInput == "8"):
            c.generateReports()
        elif (userInput == "9"):
            print("Exiting program. Thank you!")
            print("---------------------------------------------------------------------------------")
            break
        else:
            print("Input invalid. Please enter a number between 1 and 6. ")
            continue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runProgram()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
