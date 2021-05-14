DELETE FROM CoffeeShopServesFood;
DELETE FROM CoffeeShopServesDrink;
DELETE FROM EmployeeWorksAt;


-- Need to add isDeleted column in all together
ALTER TABLE CoffeeShopTable
ADD isDeleted BIT NOT NULL DEFAULT 0;

ALTER TABLE CoffeeShopServesFood
ADD isDeleted BIT NOT NULL DEFAULT 0;

ALTER TABLE CoffeeShopServesDrink
ADD isDeleted BIT NOT NULL DEFAULT 0;

ALTER TABLE DrinkTable
ADD isDeleted BIT NOT NULL DEFAULT 0;

ALTER TABLE EmployeeTable
ADD isDeleted BIT NOT NULL DEFAULT 0;

ALTER TABLE EmployeeWorksAt
ADD isDeleted BIT NOT NULL DEFAULT 0;

ALTER TABLE FoodTable
ADD isDeleted BIT NOT NULL DEFAULT 0;

ALTER TABLE StudySpotsTable
ADD isDeleted BIT NOT NULL DEFAULT 0;


-- SAMPLE PROCEDURE FROM CLASS
-- CREATE PROCEDURE getStudentInfoByZipCode(IN sZipCode CHAR(5))
-- BEGIN
--      SELECT FirstName, LastName, Street, City, ZipCode
--      FROM Student s
--      JOIN StudentAddress sa ON s.StudentId = sa.StudentId
--      WHERE sa.ZipCode = sZipcode
-- END;

-- CALL getStudentInfoByZipCode(sZipCode: '92840')





-- Procedure for option 1
CREATE PROCEDURE byDistance()
BEGIN
    SELECT CoffeeShopName, AverageDriveTimeFromChapman
    FROM CoffeeShopTable
    WHERE isDeleted = false
    ORDER BY AverageDriveTimeFromChapman ASC;
END;

-- Procedure for option 2

CREATE PROCEDURE bestStudySpots()
BEGIN
    SELECT CoffeeShopName, StudySpotsTable.WiFi, StudySpotsTable.Outlets
    FROM StudySpotsTable
    JOIN CoffeeShopTable CST on StudySpotsTable.ShopID = CST.ShopID
    WHERE WiFi = 1 AND Outlets = 1 AND CST.isDeleted = false;
END;

-- Procedure for option 3

CREATE PROCEDURE bestCustomerService()
BEGIN
    SELECT CST.CoffeeShopName, EmployeeTable.EmployeeName, EmployeeTable.EmployeeRating
    FROM EmployeeTable
    JOIN EmployeeWorksAt E ON EmployeeTable.EmployeeID = E.EmployeeID
    JOIN CoffeeShopTable CST ON E.ShopID = CST.ShopID
    WHERE EmployeeRating >= 8 AND CST.isDeleted = false AND EmployeeTable.isDeleted = false;
END;

-- Procedure for option 4

CREATE PROCEDURE cheapestDrinks()
BEGIN
    SELECT CST.CoffeeShopName, DrinkTable.DrinkName, C.Price
    FROM DrinkTable
    JOIN CoffeeShopServesDrink C ON DrinkTable.DrinkID = C.DrinkID
    JOIN CoffeeShopTable CST ON C.ShopID = CST.ShopID
    WHERE C.Price <= 5 AND CST.isDeleted = false AND DrinkTable.isDeleted = false;
END;


-- Procedure for option 5

CREATE PROCEDURE cheapestFood()
BEGIN
    SELECT CST.CoffeeShopName, FoodTable.FoodName, C.Price
    FROM FoodTable
    JOIN CoffeeShopServesFood C ON FoodTable.FoodID = C.FoodID
    JOIN CoffeeShopTable CST ON C.ShopID = CST.ShopID
    WHERE C.Price <= 5 AND CST.isDeleted = false AND FoodTable.isDeleted = false;
END;

-- Procedure for option 6

CREATE PROCEDURE bestDrinks()
BEGIN
    SELECT CST.CoffeeShopName, DrinkTable.DrinkName, C.DrinkRating
    FROM DrinkTable
    JOIN CoffeeShopServesDrink C ON DrinkTable.DrinkID = C.DrinkID
    JOIN CoffeeShopTable CST ON C.ShopID = CST.ShopID
    WHERE C.DrinkRating >= 8 AND CST.isDeleted = false AND DrinkTable.isDeleted = false;
END;

-- Procedure for option 7

CREATE PROCEDURE bestFood()
BEGIN
    SELECT CST.CoffeeShopName, FoodTable.FoodName, C.FoodRating
    FROM FoodTable
    JOIN CoffeeShopServesFood C ON FoodTable.FoodID = C.FoodID
    JOIN CoffeeShopTable CST ON C.ShopID = CST.ShopID
    WHERE C.FoodRating >= 8 AND CST.isDeleted = false AND FoodTable.isDeleted = false;
END;

-- Procedure for option 8

CREATE PROCEDURE specificDrink(IN drinkName VARCHAR(20))
BEGIN
    SELECT CST.CoffeeShopName, DrinkTable.DrinkName
    FROM DrinkTable
    JOIN CoffeeShopServesDrink C ON DrinkTable.DrinkID = C.DrinkID
    JOIN CoffeeShopTable CST ON C.ShopID = CST.ShopID
    WHERE DrinkTable.DrinkName = drinkName AND CST.isDeleted = false AND DrinkTable.isDeleted = false;
END;

-- Transaction for create new record

CREATE PROCEDURE createCoffeeShop(IN shopName VARCHAR(50), IN phoneNum VARCHAR(25), IN driveTime VARCHAR(3), IN w INT, IN s INT, IN o INT, IN m INT)
BEGIN
    DECLARE should_rollback BOOL DEFAULT FALSE;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET should_rollback = TRUE;

    START TRANSACTION;

    INSERT INTO CoffeeShopTable(CoffeeShopName, PhoneNumber, AverageDriveTimeFromChapman)
    VALUES (shopName, phoneNum, driveTime);

    INSERT INTO StudySpotsTable(ShopID, Wifi, IndoorSeating, Outlets, Music)
    VALUES ((SELECT ShopID FROM CoffeeShopTable WHERE CoffeeShopName = shopName), w, s, o, m);

    IF should_rollback THEN
        ROLLBACK;
    ELSE
        COMMIT;
    end if;
END;


DROP PROCEDURE createCoffeeShop;

CALL createCoffeeShop( 'Test', '1234', '30', 'hello',  1, 1, 1);

-- Views for the generate report portion

DROP VIEW avgDrinkRating;
DROP VIEW avgFoodRating;
DROP VIEW avgDrinkPrice;
DROP VIEW avgFoodPrice;

-- Report #2: Average Drink Ratings at each coffee shop
CREATE VIEW avgDrinkRating AS
    SELECT CST.CoffeeShopName, AVG(C.DrinkRating)
    FROM DrinkTable
    JOIN CoffeeShopServesDrink C ON DrinkTable.DrinkID = C.DrinkID
    JOIN CoffeeShopTable CST ON C.ShopID = CST.ShopID
    WHERE CST.isDeleted = false AND DrinkTable.isDeleted = false
    GROUP BY CoffeeShopName;



-- Report #3: Average Food Ratings at each coffee shop

CREATE VIEW avgFoodRating AS
    SELECT CST.CoffeeShopName, AVG(C.FoodRating)
    FROM FoodTable
    JOIN CoffeeShopServesFood C ON FoodTable.FoodID = C.FoodID
    JOIN CoffeeShopTable CST ON C.ShopID = CST.ShopID
    WHERE CST.isDeleted = false AND FoodTable.isDeleted = false
    GROUP BY CoffeeShopName;

-- Report #4: Average Drink Price at each coffee shop

CREATE VIEW avgDrinkPrice AS
    SELECT CST.CoffeeShopName, AVG(C.Price)
    FROM DrinkTable
    JOIN CoffeeShopServesDrink C ON DrinkTable.DrinkID = C.DrinkID
    JOIN CoffeeShopTable CST ON C.ShopID = CST.ShopID
    WHERE CST.isDeleted = false AND DrinkTable.isDeleted = false
    GROUP BY CoffeeShopName;

-- Report #5: Average Food Price at each coffee shop

CREATE VIEW avgFoodPrice AS
    SELECT CST.CoffeeShopName, AVG(C.Price)
    FROM FoodTable
    JOIN CoffeeShopServesFood C ON FoodTable.FoodID = C.FoodID
    JOIN CoffeeShopTable CST ON C.ShopID = CST.ShopID
    WHERE CST.isDeleted = false AND FoodTable.isDeleted = false
    GROUP BY CoffeeShopName;



DROP VIEW updateDrinkQuery;
DROP VIEW updateFoodQuery;

CREATE VIEW updateDrinkQuery AS
    SELECT CST.ShopID, CST.CoffeeShopName, C.DrinkServedID, DrinkTable.DrinkName, C.Price, C.DrinkRating
    FROM DrinkTable
    JOIN CoffeeShopServesDrink C ON DrinkTable.DrinkID = C.DrinkID
    JOIN CoffeeShopTable CST ON C.ShopID = CST.ShopID
    WHERE CST.isDeleted = false and DrinkTable.isDeleted = false;

CREATE VIEW updateFoodQuery AS
    SELECT CST.ShopID, CST.CoffeeShopName, C.FoodServedID, FoodTable.FoodName, C.Price, C.FoodRating
    FROM FoodTable
    JOIN CoffeeShopServesFood C ON FoodTable.FoodID = C.FoodID
    JOIN CoffeeShopTable CST ON C.ShopID = CST.ShopID
    WHERE CST.isDeleted = false AND FoodTable.isDeleted = false;

CREATE VIEW updateEmployeeQuery AS
    SELECT CST.ShopID, CST.CoffeeShopName, EmployeeTable.EmployeeID, EmployeeTable.EmployeeName, EmployeeTable.EmployeeRating, EmployeeTable.ReviewDescription
    FROM EmployeeTable
    JOIN EmployeeWorksAt E ON EmployeeTable.EmployeeID = E.EmployeeID
    JOIN CoffeeShopTable CST ON E.ShopID = CST.ShopID
    WHERE CST.isDeleted = false AND EmployeeTable.isDeleted = false;


-- Create indexes on the columns that I join frequently which are EmployeeID, FoodID, and DrinkID

CREATE INDEX idx_employee
ON EmployeeTable(EmployeeID);

CREATE INDEX idx_employee1
ON EmployeeWorksAt(EmployeeID, ShopID);

CREATE INDEX idx_food
ON FoodTable(FoodID);

CREATE INDEX idx_food1
ON CoffeeShopServesFood(FoodID,ShopID);

CREATE INDEX idx_drink
ON DrinkTable(DrinkID);

CREATE INDEX idx_drink1
ON CoffeeShopServesDrink(DrinkID, ShopID);

CREATE INDEX idx_shop1
ON CoffeeShopTable(ShopID);