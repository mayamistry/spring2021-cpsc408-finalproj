import mysql.connector
from faker import Faker
import csv
import pandas as pd
from pandas import DataFrame

db = mysql.connector.connect(
    host = "35.236.58.10",
    user = "myappuser",
    password = "foobar",
    database = "CoffeeShopDB"
)

def printMenu():
    print("Here is what you can do with the Coffee Shop Database: ")
    print("(1) - Display all information from the database")
    print("(2) - Filtered results from the database")
    print("(3) - Add a new coffee shop to the database")
    print("(4) - Delete a coffee shop from the database")
    print("(5) - Update information about a specific coffee shop")
    print("(6) - Update the price and rating of a drink item from a specific coffee shop")
    print("(7) - Update the price and rating of a food item from a specific coffee shop")
    print("(8) - Update information about an employee from a specific coffee shop")
    print("(9) - Add food items that a specific coffee shop serves")
    print("(10) - Add drink items that a specific coffee shop serves")
    print("(11) - Add an employee that works at a specific coffee shop")
    print("(12) - Generate CSV file reports")
    print("(13) - Quit application")

#1 - Function to print and display all records from database/tables
# STATUS - DONE
def displayRecords():
    mycursor = db.cursor()
    print("Table Name: CoffeeShopTable")
    #Coffee Shop Table
    mycursor.execute("SELECT ShopID, CoffeeShopName, PhoneNumber, AverageDriveTimeFromChapman FROM CoffeeShopTable WHERE isDeleted = false;")
    shops = mycursor.fetchall()
    # This function below actually  prints out all rows and columns instead of just a few - found online
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df = DataFrame(shops,
                   columns=['Shop ID','Coffee Shop Name', 'Phone Number', 'Average Drive Time From Chapman'])
    print(df)
    print("---------------------------------------------------------------------------------")

    #StudySpotsTable
    print("Table Name: StudySpotsTable")
    mycursor.execute("SELECT StudyID, ShopID, WiFi, IndoorSeating, Outlets, Music FROM StudySpotsTable WHERE isDeleted = false;")
    shops = mycursor.fetchall()
    # This function below actually  prints out all rows and columns instead of just a few - found online
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df = DataFrame(shops,
                   columns=['Study ID', 'Shop ID', 'WiFi?', 'Indoor Seating?', 'Outlets?', 'Music?'])
    print(df)
    print("---------------------------------------------------------------------------------")

    #FoodTable
    print("Table Name: FoodTable")
    mycursor.execute("SELECT FoodID, FoodName FROM FoodTable WHERE isDeleted = false;")
    shops = mycursor.fetchall()
    # This function below actually  prints out all rows and columns instead of just a few - found online
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df = DataFrame(shops,
                   columns=['Food ID', 'Food Name'])
    print(df)
    print("---------------------------------------------------------------------------------")

    #DrinkTable
    print("Table Name: DrinkTable")
    mycursor.execute("SELECT DrinkID, DrinkName FROM DrinkTable WHERE isDeleted = false;")
    shops = mycursor.fetchall()
    # This function below actually  prints out all rows and columns instead of just a few - found online
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df = DataFrame(shops,
                   columns=['Drink ID', 'Drink Name'])
    print(df)
    print("---------------------------------------------------------------------------------")

    #EmployeeTable
    print("Table Name: EmployeeTable")
    mycursor.execute("SELECT EmployeeID, EmployeeName, EmployeeRating, ReviewDescription FROM EmployeeTable WHERE isDeleted = false;")
    shops = mycursor.fetchall()
    # This function below actually  prints out all rows and columns instead of just a few - found online
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df = DataFrame(shops,
                   columns=['Employee ID', 'Employee Name', 'Employee Rating', 'Review Description'])
    print(df)
    print("---------------------------------------------------------------------------------")

    #CoffeeShopServesDrink
    print("Table Name: CoffeeShopServesDrink")
    mycursor.execute("SELECT DrinkServedID, DrinkID, ShopID, DrinkRating, Price FROM CoffeeShopServesDrink WHERE isDeleted = false;")
    shops = mycursor.fetchall()
    # This function below actually  prints out all rows and columns instead of just a few - found online
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df = DataFrame(shops,
                   columns=['Drink Served ID', 'Drink ID', 'Shop ID', 'DrinkRating', 'Price'])
    print(df)
    print("---------------------------------------------------------------------------------")

    # CoffeeShopServesFood
    print("Table Name: CoffeeShopServesFood")
    mycursor.execute("SELECT FoodServedID, FoodID, ShopID, FoodRating, Price FROM CoffeeShopServesFood WHERE isDeleted = false;")
    shops = mycursor.fetchall()
    # This function below actually  prints out all rows and columns instead of just a few - found online
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df = DataFrame(shops,
                   columns=['Food Served ID', 'Food ID', 'Shop ID', 'FoodRating', 'Price'])
    print(df)
    print("---------------------------------------------------------------------------------")

    #EmployeeWorksAt
    print("Table Name: EmployeeWorksAt")
    mycursor.execute("SELECT WorksID, EmployeeID, ShopID FROM EmployeeWorksAt WHERE isDeleted = false;")
    shops = mycursor.fetchall()
    # This function below actually  prints out all rows and columns instead of just a few - found online
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df = DataFrame(shops,
                   columns=['Works ID', 'Employee ID', 'Shop ID'])
    print(df)
    print("---------------------------------------------------------------------------------")


#2 - Function to query data with different parameters
#STATUS - DONE
def parameterQueries():
    mycursor = db.cursor()
    print("What type of results would you like to print out from the database?")
    #All of the filters
    print("(1) - Coffee Shops organized by distance")
    print("(2) - Coffee Shops that are the best study spots")
    print("(3) - Coffee Shops with great customer service")
    print("(4) - Coffee Shops with the cheapest drinks")
    print("(5) - CCoffee Shops with the cheapest food")
    print("(6) - Coffee Shops with the best drinks")
    print("(7) - Coffee Shops with the best food")
    print("(8) - Coffee Shops with this specific drink: ___")
    status = False
    while (status == False):
        userChoice = int(input("Enter the numerical value of which option you would like to choose: "))
        if (userChoice == 1):
            mycursor.callproc('byDistance')
            distance = 0
            for result in mycursor.stored_results():
                distance = result.fetchall()
            df = pd.DataFrame(distance, columns = ['Coffee Shop Name', 'Average Drive Time From Chapman'])
            print(df)
            status = True
        elif (userChoice == 2):
            mycursor.callproc('bestStudySpots')
            study = 0
            for result in mycursor.stored_results():
                study = result.fetchall()
            df = pd.DataFrame(study, columns=['Coffee Shop Name', 'WiFi?', 'Outlets?'])
            print(df)
            status = True
        elif (userChoice == 3):
            mycursor.callproc('bestCustomerService')
            service = 0
            for result in mycursor.stored_results():
                service = result.fetchall()
            df = pd.DataFrame(service, columns=['Coffee Shop Name', 'Employee Name', 'Employee Rating'])
            print(df)
            status = True
        elif (userChoice == 4):
            mycursor.callproc('cheapestDrinks')
            cheap = 0
            for result in mycursor.stored_results():
                cheap = result.fetchall()
            df = pd.DataFrame(cheap, columns=['Coffee Shop Name', 'Drink Name', 'Price'])
            print(df)
            status = True
        elif (userChoice == 5):
            mycursor.callproc('cheapestFood')
            cheap1 = 0
            for result in mycursor.stored_results():
                cheap1 = result.fetchall()
            df = pd.DataFrame(cheap1, columns=['Coffee Shop Name', 'Food Name', 'Price'])
            print(df)
            status = True
        elif (userChoice == 6):
            mycursor.callproc('bestDrinks')
            best = 0
            for result in mycursor.stored_results():
                best = result.fetchall()
            df = pd.DataFrame(best, columns=['Coffee Shop Name', 'Drink Name', 'Rating'])
            print(df)
            status = True
        elif (userChoice == 7):
            mycursor.callproc('bestFood')
            best1 = 0
            for result in mycursor.stored_results():
                best1 = result.fetchall()
            df = pd.DataFrame(best1, columns=['Coffee Shop Name', 'Food Name', 'Rating'])
            print(df)
            status = True
        elif (userChoice == 8):
            drinkName = input("What kind of drink are you looking for?: ")
            mycursor.callproc('specificDrink', [drinkName])
            drink = 0
            for result in mycursor.stored_results():
                drink = result.fetchall()
            df = pd.DataFrame(drink, columns=['Coffee Shop Name', 'Drink Name'])
            if (len(df.index) == 0):
                print("No coffee shops have the drink you searched for.")
            else:
                print(df)
            status = True
        else:
            print("Error: please choose one of the numerical options provided.")
    print("---------------------------------------------------------------------------------")


#3 - Function to create a new record
# STATUS - FIRST ONE FIGURED OUT AND NEED TO DO THE REST - might be a little tough...
# Doing transactions with this one
def createNewRecord():
    mycursor = db.cursor()
    #For right now, only do it for the CoffeeShopTable
    shopName = input("Enter the name of the new coffee shop: ")
    phoneNumber = input("Enter the phone number for the coffee shop: ")
    driveTime = input("Enter the average drive time from Chapman: ")
    while (driveTime.isalpha() == True):
        driveTime = input("Error. Please try again and enter a numerical value for drive time: ")
    status = False
    while (status == False):
        try:
            wifi = int(input("Does this coffee shop have WiFi? Enter 1 for yes and 0 for no: "))
            if (wifi == 1 or wifi == 0):
                status = True
            else:
                print("Error: please enter a 1 or 0.")
                continue
        except (ValueError):
            print("Error: please enter an integer of either 1 or 0.")
    status = False
    while (status == False):
        try:
            seating = int(input("Does this coffee shop have indoor seating? Enter 1 for yes and 0 for no: "))
            if (seating == 1 or seating == 0):
                status = True
            else:
                print("Error: please enter a 1 or 0.")
                continue
        except (ValueError):
            print("Error: please enter an integer of either 1 or 0.")
    status = False
    while (status == False):
        try:
            outlets = int(input("Does this coffee shop have outlets? Enter 1 for yes and 0 for no: "))
            if (outlets == 1 or outlets == 0):
                status = True
            else:
                print("Error: please enter a 1 or 0.")
                continue
        except (ValueError):
            print("Error: please enter an integer of either 1 or 0.")
    status = False
    while (status == False):
        try:
            music = int(input("Does this coffee shop have music? Enter 1 for yes and 0 for no: "))
            if (music == 1 or music == 0):
                status = True
            else:
                print("Error: please enter a 1 or 0.")
                continue
        except (ValueError):
            print("Error: please enter an integer of either 1 or 0.")
    #Call the procedure after gathering all of the information
    mycursor.callproc('createCoffeeShop', [shopName, phoneNumber, driveTime, wifi, seating, outlets, music])
    print("Successfully added the new coffee shop to the database!")
    print("---------------------------------------------------------------------------------")



#4 - Function  that performs a soft delete on any of the tables
# STATUS - DONE
def deleteRecord():
    mycursor = db.cursor()
    displayRecords()
    print("Here are all of the tables you can delete from: CoffeeShopTable, DrinkTable, FoodTable, and EmployeeTable")
    table = input("Which table would you like to delete a record from? ")
    status = False
    while (status == False):
        if (table == "CoffeeShopTable"):
            status1 = False
            while (status1 == False):
                checkID = input("Enter the ID of the coffee shop you want to delete: ")
                mycursor.execute("SELECT * FROM CoffeeShopTable WHERE ShopID = %s", [checkID])
                data = mycursor.fetchall()
                #If the ID the user entered does not exist in the table, then they need to keep trying again until they get it right
                if data == []:
                    print("ShopID entered is invalid, please try again.")
                    continue
                else:
                    status1 = True
                    mycursor.execute("UPDATE CoffeeShopTable SET isDeleted = true WHERE ShopID = %s", [checkID])
                    db.commit()
                    print("Successfully deleted the coffee shop!")
                    break
            status = True
        elif (table == "DrinkTable"):
            status2 = False
            while (status2 == False):
                checkID = input("Enter the ID of the drink  you want to delete: ")
                mycursor.execute("SELECT * FROM DrinkTable WHERE DrinkID = %s", [checkID])
                data = mycursor.fetchall()
                # If the ID the user entered does not exist in the table, then they need to keep trying again until they get it right
                if data == []:
                    print("DrinkID entered is invalid, please try again.")
                    continue
                else:
                    status2 = True
                    mycursor.execute("UPDATE DrinkTable SET isDeleted = true WHERE DrinkID = %s", [checkID])
                    db.commit()
                    print("Successfully deleted the drink!")
                    break
            status = True
        elif (table == "EmployeeTable"):
            status3 = False
            while (status3 == False):
                checkID = input("Enter the ID of the employee you want to delete: ")
                mycursor.execute("SELECT * FROM EmployeeTable WHERE EmployeeID = %s", [checkID])
                data = mycursor.fetchall()
                # If the ID the user entered does not exist in the table, then they need to keep trying again until they get it right
                if data == []:
                    print("EmployeeID entered is invalid, please try again.")
                    continue
                else:
                    status3 = True
                    mycursor.execute("UPDATE EmployeeTable SET isDeleted = true WHERE EmployeeID = %s", [checkID])
                    db.commit()
                    print("Successfully deleted the employee!")
                    break
            status = True
        elif (table == "FoodTable"):
            status4 = False
            while (status4 == False):
                checkID = input("Enter the ID of the coffee shop you want to delete: ")
                mycursor.execute("SELECT * FROM FoodTable WHERE FoodID = %s", [checkID])
                data = mycursor.fetchall()
                # If the ID the user entered does not exist in the table, then they need to keep trying again until they get it right
                if data == []:
                    print("FoodID entered is invalid, please try again.")
                    continue
                else:
                    status4 = True
                    mycursor.execute("UPDATE FoodTable SET isDeleted = true WHERE FoodID = %s", [checkID])
                    db.commit()
                    print("Successfully deleted the food item!")
                    break
            status = True
        else:
            table = input("Table name you entered does not exist, please try again: ")
    print("---------------------------------------------------------------------------------")



#STATUS - NOT FIGURED OUT AT ALL
def updateRecord():
    mycursor = db.cursor()
    mycursor.execute(
        "SELECT ShopID, CoffeeShopName, PhoneNumber, AverageDriveTimeFromChapman FROM CoffeeShopTable WHERE isDeleted = false;")
    shops = mycursor.fetchall()
    # This function below actually  prints out all rows and columns instead of just a few - found online
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df = DataFrame(shops,
                   columns=['Shop ID', 'Coffee Shop Name', 'Phone Number', 'Average Drive Time From Chapman'])
    print(df)
    status = False
    shopID = 0
    while (status == False):
        try:
            shopID = int(input("Enter the ID for which coffee shop you would like to update: "))
            mycursor.execute("SELECT * FROM CoffeeShopTable WHERE ShopID = %s AND isDeleted = false", [shopID])
            data = mycursor.fetchall()
            if (data == []):
                print("Error: the ID you entered does not exist. Please try again.")
                continue
            else:
                status = True
        except (ValueError):
            print("Error: please an integer")
    status = False
    while (status == False):
        try:
            userInput = int(input("Would you like to update this coffee shop's name? Enter 1 for yes and 0 for no: "))
            if (userInput == 1):
                #run the query here
                newName =  input("Enter the new name for this coffee shop: ")
                mycursor.execute("UPDATE CoffeeShopTable SET CoffeeShopName = %s WHERE ShopID = %s", (newName, shopID))
                db.commit()
                status = True
            elif (userInput == 0):
                status = True
            else:
                print("Error: please enter only a 1 or 0")
                continue
        except (ValueError):
            print("Error: please enter an integer of either 1 or 0.")
    status = False
    while (status == False):
        try:
            userInput = int(input("Would you like to update this coffee shop's phone number? Enter 1 for yes and 0 for no: "))
            if (userInput == 1):
                # run the query here
                newNumber = input("Enter the new phone number for this coffee shop: ")
                mycursor.execute("UPDATE CoffeeShopTable SET PhoneNumber = %s WHERE ShopID = %s", (newNumber, shopID))
                db.commit()
                status = True
            elif (userInput == 0):
                status = True
            else:
                print("Error: please enter only a 1 or 0")
                continue
        except (ValueError):
            print("Error: please enter an integer of either 1 or 0.")
    status = False
    while (status == False):
        try:
            userInput = int(input("Would you like to update this coffee shop's average drive time from Chapman? Enter 1 for yes and 0 for no: "))
            if (userInput == 1):
                # run the query here
                newDrive = input("Enter the new average drive time from Chapman for this coffee shop: ")
                mycursor.execute("UPDATE CoffeeShopTable SET AverageDriveTimeFromChapman = %s WHERE ShopID = %s", (newDrive, shopID))
                db.commit()
                status = True
            elif (userInput == 0):
                status = True
            else:
                print("Error: please enter only a 1 or 0")
                continue
        except (ValueError):
            print("Error: please enter an integer of either 1 or 0.")
    print("Successfully made all of the updates for this coffee shop!")
    print("---------------------------------------------------------------------------------")

def updateDrink():
    mycursor  = db.cursor()
    mycursor.execute("SELECT * FROM updateDrinkQuery");
    shops = mycursor.fetchall()
    # This function below actually  prints out all rows and columns instead of just a few - found online
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df = DataFrame(shops,
                   columns=['Shop ID', 'Coffee Shop Name', 'Drink Served ID', 'Drink Name', 'Drink Price', 'Drink Rating'])
    print(df)
    status = False
    shopID = 0
    drinkID = 0
    while (status == False):
        try:
            shopID = int(input("Enter the Shop ID you are updating the drink for: "))
            drinkID = int(input("Enter the Drink Served ID that corresponds with the Shop ID: "))
            mycursor.execute("SELECT * FROM updateDrinkQuery WHERE ShopID = %s AND DrinkServedID = %s", (shopID, drinkID))
            data = mycursor.fetchall()
            if (data == []):
                print("Error: the IDs you entered do not exist. Please try again.")
                continue
            else:
                newPrice = int(input("Enter the new price for this drink: "))
                newRating = int(input("Enter the new rating for this drink: "))
                mycursor.execute("UPDATE CoffeeShopServesDrink SET Price = %s, DrinkRating = %s WHERE DrinkServedID = %s",
                                 (newPrice, newRating, drinkID))
                db.commit()
                status = True
        except (ValueError):
            print("Error: please an integer")
    print("Successfully updated the drink!")
    print("---------------------------------------------------------------------------------")



def updateFood():
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM updateFoodQuery");
    shops = mycursor.fetchall()
    # This function below actually  prints out all rows and columns instead of just a few - found online
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df = DataFrame(shops,
                   columns=['Shop ID', 'Coffee Shop Name', 'Food Served ID', 'Food Name', 'Food Price',
                            'Food Rating'])
    print(df)
    status = False
    shopID = 0
    foodID = 0
    while (status == False):
        try:
            shopID = int(input("Enter the Shop ID you are updating the drink for: "))
            foodID = int(input("Enter the Food Served ID that corresponds with the Shop ID: "))
            mycursor.execute("SELECT * FROM updateFoodQuery WHERE ShopID = %s AND FoodServedID = %s",
                             (shopID, foodID))
            data = mycursor.fetchall()
            if (data == []):
                print("Error: the IDs you entered do not exist. Please try again.")
                continue
            else:
                newPrice = int(input("Enter the new price for this food item: "))
                newRating = int(input("Enter the new rating for this food item: "))
                mycursor.execute("UPDATE CoffeeShopServesFood SET Price = %s, FoodRating = %s WHERE FoodServedID = %s",
                                 (newPrice, newRating, foodID))
                db.commit()
                status = True
        except (ValueError):
            print("Error: please an integer")
    print("Successfully updated the food item!")
    print("---------------------------------------------------------------------------------")

def updateEmployee():
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM updateEmployeeQuery");
    shops = mycursor.fetchall()
    # This function below actually  prints out all rows and columns instead of just a few - found online
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df = DataFrame(shops,
                   columns=['Shop ID', 'Coffee Shop Name', 'Employee ID', 'Employee Name', 'Employee Rating',
                            'Review Description'])
    print(df)
    status = False
    employeeID = 0
    while (status == False):
        try:
            employeeID = int(input("Enter the Employee ID that you would like to update: "))
            mycursor.execute("SELECT * FROM updateEmployeeQuery WHERE EmployeeID = %s",
                             [employeeID])
            data = mycursor.fetchall()
            if (data == []):
                print("Error: the IDs you entered do not exist. Please try again.")
                continue
            else:
                newRating = int(input("Enter the new rating for this employee: "))
                newDescription = input("Enter a new review description for this employee: ")
                mycursor.execute("UPDATE EmployeeTable SET  EmployeeRating = %s, ReviewDescription = %s WHERE EmployeeID = %s",
                                 (newRating, newDescription, employeeID))
                db.commit()
                status = True
        except (ValueError):
            print("Error: please an integer")
    print("Successfully updated the employee!")
    print("---------------------------------------------------------------------------------")

def addEmployee():
    overallCheck = False
    while (overallCheck == False):
        mycursor = db.cursor()
        mycursor.execute(
            "SELECT ShopID, CoffeeShopName, PhoneNumber, AverageDriveTimeFromChapman FROM CoffeeShopTable WHERE isDeleted = false;")
        shops = mycursor.fetchall()
        # This function below actually  prints out all rows and columns instead of just a few - found online
        pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
        df = DataFrame(shops,
                       columns=['Shop ID', 'Coffee Shop Name', 'Phone Number', 'Average Drive Time From Chapman'])
        print(df)
        status = False
        shopID = 0
        while (status == False):
            try:
                shopID = int(input("Enter the ID for which coffee shop you would like to add an employee for: "))
                mycursor.execute("SELECT * FROM CoffeeShopTable WHERE ShopID = %s AND isDeleted = false", [shopID])
                data = mycursor.fetchall()
                if (data == []):
                    print("Error: the ID you entered does not exist. Please try again.")
                    continue
                else:
                    status = True
            except (ValueError):
                print("Error: please an integer")
        # First add the employee to employee table and then add to the works at table
        status = False
        while (status == False):
            try:
                employeeName = input("Enter the name of this new employee: ")
                employeeRating = int(input("Enter the rating for this employee: "))
                description = input("Provide a review description for this employee: ")
                mycursor.execute("INSERT INTO EmployeeTable(EmployeeName, EmployeeRating, ReviewDescription) VALUES (%s, %s, %s)",
                    (employeeName, employeeRating, description))
                employeeID = mycursor.lastrowid
                mycursor.execute("INSERT INTO EmployeeWorksAt(EmployeeID, ShopID) VALUES (%s, %s)", (employeeID, shopID))
                db.commit()
                status = True
            except (ValueError):
                print("Error: please enter an integer of either 1 or 0.")
        print("Successfully add this employee to the database for this coffee shop!")
        print("\n")
        status = False
        while (status == False):
            try:
                check = int(input(
                    "Would you like to continue adding food items to a coffee shop? Enter 1 for yes and 0 for no: "))
                if (check == 1):
                    status = True
                elif (check == 0):
                    overallCheck = True
                    status = True
                else:
                    print("Error: please enter only a 1 or 0")
                    continue
            except (ValueError):
                print("Error: please enter an integer of either 1 or 0.")
    print("---------------------------------------------------------------------------------")

def addFood():
    overallCheck = False
    while (overallCheck == False):
        mycursor = db.cursor()
        mycursor.execute(
            "SELECT ShopID, CoffeeShopName, PhoneNumber, AverageDriveTimeFromChapman FROM CoffeeShopTable WHERE isDeleted = false;")
        shops = mycursor.fetchall()
        # This function below actually  prints out all rows and columns instead of just a few - found online
        pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
        df = DataFrame(shops,
                       columns=['Shop ID', 'Coffee Shop Name', 'Phone Number', 'Average Drive Time From Chapman'])
        print(df)
        status = False
        shopID = 0
        while (status == False):
            try:
                shopID = int(input("Enter the ID for which coffee shop you would like to add a food item for: "))
                mycursor.execute("SELECT * FROM CoffeeShopTable WHERE ShopID = %s AND isDeleted = false", [shopID])
                data = mycursor.fetchall()
                if (data == []):
                    print("Error: the ID you entered does not exist. Please try again.")
                    continue
                else:
                    status = True
            except (ValueError):
                print("Error: please an integer")
        #First check if any of the foods are from the original food list
        mycursor.execute(
            "SELECT FoodID, FoodName FROM FoodTable WHERE isDeleted = false;")
        shops = mycursor.fetchall()
        # This function below actually  prints out all rows and columns instead of just a few - found online
        pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
        df = DataFrame(shops,
                       columns=['Food ID', 'Food Name'])
        print(df)
        status = False
        while (status == False):
            try:
                foodExist = int(input("Does the food item you want to add already exits in this table above? Enter 1 for yes and 0 for no: "))
                if (foodExist == 1):
                    # run the query here
                    foodID = int(input("Enter the food ID that you would like to add for this coffee shop: "))
                    foodRating = int(input("Enter the rating of this food item at this specific coffee shop: "))
                    price = int(input("Enter the price of this food item at this specific coffee shop: "))
                    mycursor.execute("INSERT INTO CoffeeShopServesFood(ShopID, FoodID, FoodRating, Price) VALUES (%s, %s, %s, %s)", (shopID, foodID, foodRating, price))
                    db.commit()
                    status = True
                elif (foodExist == 0):
                    #Need to add another food item to food table
                    foodName = input("Enter the name of the new food item you're adding: ")
                    # add new food to the food table and grab it's ID
                    mycursor.execute("INSERT INTO FoodTable(FoodName) VALUES (%s)", [foodName])
                    db.commit()
                    foodID = mycursor.lastrowid
                    foodRating = int(input("Enter the rating of this food item at this specific coffee shop: "))
                    price = int(input("Enter the price of this food item at this specific coffee shop: "))
                    mycursor.execute(
                        "INSERT INTO CoffeeShopServesFood(ShopID, FoodID, FoodRating, Price) VALUES (%s, %s, %s, %s)", (shopID, foodID, foodRating, price))
                    db.commit()
                    status = True
                else:
                    print("Error: please enter only a 1 or 0")
                    continue
            except (ValueError):
                print("Error: please enter an integer of either 1 or 0.")
        print("Successfully add this food item to the database for this coffee shop!")
        print("\n")
        status = False
        while (status == False):
            try:
                check = int(input("Would you like to continue adding food items to a coffee shop? Enter 1 for yes and 0 for no: "))
                if (check == 1):
                    status = True
                elif (check == 0):
                    overallCheck = True
                    status = True
                else:
                    print("Error: please enter only a 1 or 0")
                    continue
            except (ValueError):
                print("Error: please enter an integer of either 1 or 0.")
    print("---------------------------------------------------------------------------------")


def addDrink():
    overallCheck = False
    while (overallCheck == False):
        mycursor = db.cursor()
        mycursor.execute(
            "SELECT ShopID, CoffeeShopName, PhoneNumber, AverageDriveTimeFromChapman FROM CoffeeShopTable WHERE isDeleted = false;")
        shops = mycursor.fetchall()
        # This function below actually  prints out all rows and columns instead of just a few - found online
        pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
        df = DataFrame(shops,
                       columns=['Shop ID', 'Coffee Shop Name', 'Phone Number', 'Average Drive Time From Chapman'])
        print(df)
        status = False
        shopID = 0
        while (status == False):
            try:
                shopID = int(input("Enter the ID for which coffee shop you would like to add a drink item for: "))
                mycursor.execute("SELECT * FROM CoffeeShopTable WHERE ShopID = %s AND isDeleted = false", [shopID])
                data = mycursor.fetchall()
                if (data == []):
                    print("Error: the ID you entered does not exist. Please try again.")
                    continue
                else:
                    status = True
            except (ValueError):
                print("Error: please an integer")
        # First check if any of the foods are from the original food list
        mycursor.execute(
            "SELECT DrinkID, DrinkName FROM DrinkTable WHERE isDeleted = false;")
        shops = mycursor.fetchall()
        # This function below actually  prints out all rows and columns instead of just a few - found online
        pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
        df = DataFrame(shops,
                       columns=['Drink ID', 'Drink Name'])
        print(df)
        status = False
        while (status == False):
            try:
                drinkExist = int(input(
                    "Does the drink item you want to add already exits in this table above? Enter 1 for yes and 0 for no: "))
                if (drinkExist == 1):
                    # run the query here
                    drinkID = int(input("Enter the drink ID that you would like to add for this coffee shop: "))
                    drinkRating = int(input("Enter the rating of this drink item at this specific coffee shop: "))
                    price = int(input("Enter the price of this drink item at this specific coffee shop: "))
                    mycursor.execute(
                        "INSERT INTO CoffeeShopServesDrink(ShopID, DrinkID, DrinkRating, Price) VALUES (%s, %s, %s, %s)",
                        (shopID, drinkID, drinkRating, price))
                    db.commit()
                    status = True
                elif (drinkExist == 0):
                    # Need to add another drink item to drink table
                    drinkName = input("Enter the name of the new drink item you're adding: ")
                    # add new drink to the drink table and grab it's ID
                    mycursor.execute("INSERT INTO DrinkTable(DrinkName) VALUES (%s)", [drinkName])
                    db.commit()
                    drinkID = mycursor.lastrowid
                    drinkRating = int(input("Enter the rating of this drink item at this specific coffee shop: "))
                    price = int(input("Enter the price of this drink item at this specific coffee shop: "))
                    mycursor.execute(
                        "INSERT INTO CoffeeShopServesDrink(ShopID, DrinkID, DrinkRating, Price) VALUES (%s, %s, %s, %s)",
                        (shopID, drinkID, drinkRating, price))
                    db.commit()
                    status = True
                else:
                    print("Error: please enter only a 1 or 0")
                    continue
            except (ValueError):
                print("Error: please enter an integer of either 1 or 0.")
        print("Successfully add this drink  item to the database for this coffee shop!")
        print("\n")
        status = False
        while (status == False):
            try:
                check = int(input(
                    "Would you like to continue adding drink items to a coffee shop? Enter 1 for yes and 0 for no: "))
                if (check == 1):
                    status = True
                elif (check == 0):
                    overallCheck = True
                    status = True
                else:
                    print("Error: please enter only a 1 or 0")
                    continue
            except (ValueError):
                print("Error: please enter an integer of either 1 or 0.")
    print("---------------------------------------------------------------------------------")

#STATUS - DONE
def generateReports():
    #Report 1 - generating the best study spots csv file
    mycursor = db.cursor()
    mycursor.callproc('bestStudySpots')
    study = 0
    for result in mycursor.stored_results():
        study = result.fetchall()
    df = pd.DataFrame(study, columns=['CoffeeShopName', 'WiFi', 'Outlets'])
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df.to_csv('BestStudySpots_Report.csv')

    #Report 2 - average drink rating at each coffee shop
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM avgDrinkRating")
    drink = mycursor.fetchall()
    df = pd.DataFrame(drink, columns=['CoffeeShopName', 'Avg Drink Rating'])
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df.to_csv('AverageDrinkRatingPerCoffeeShop_Report.csv')

    #Report 3 - average food rating at each coffee shop
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM avgFoodRating")
    food = mycursor.fetchall()
    df = pd.DataFrame(food, columns=['CoffeeShopName', 'Avg Food Rating'])
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df.to_csv('AverageFoodRatingPerCoffeeShop.csv')

    # Report 4 - average drink price at each coffee shop
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM avgDrinkPrice")
    drink1 = mycursor.fetchall()
    df = pd.DataFrame(drink1, columns=['CoffeeShopName', 'Avg Drink Price'])
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df.to_csv('AverageDrinkPricePerCoffeeShop_Report.csv')

    # Report 5 - average food price at each coffee shop
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM avgFoodPrice")
    food = mycursor.fetchall()
    df = pd.DataFrame(food, columns=['CoffeeShopName', 'Avg Food Price'])
    pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)
    df.to_csv('AverageFoodPricePerCoffeeShop.csv')

    print("Successfully created all reports! Refer to your local machine to view these reports.")
    print("Here are the reports that were created: ")
    print("Report 1: Best Coffee Shops for Studying (WiFi and Outlets)")
    print("Report 2: Average drink rating for each coffee shop")
    print("Report 3: Average food rating for each coffee shop")
    print("Report 4: Average drink price for each coffee shop")
    print("Report 5: Average food price for each coffee shop")
    print("---------------------------------------------------------------------------------")






