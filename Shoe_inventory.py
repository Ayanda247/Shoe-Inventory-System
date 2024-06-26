#!/usr/bin/env python3
# Import Modules.
from io import FileIO
import os
import time
import sys

# Dictionary of Continents
continents = {
    "North America": [
        "Haiti",
        "United States of America",
        "Canada",
        "Mexico",
        "Guatemala",
        "Belize",
        "El Salvador",
        "Honduras",
        "Nicaragua",
        "Costa Rica",
        "Panama",
        "Cuba",
        "Jamaica",
        "Dominican Republic",
        "Dominica",
        "Saint Kitts and Nevis",
        "Saint Vincent and the Grenadines",
        "Antigua and Barbuda",
        "Saint Lucia",
        "Barbados",
        "Trinidad and Tobago",
        "The Bahamas",
        "Grenada",
    ],
    "South America": [
        "Argentina",
        "Bolivia",
        "Brazil",
        "Chile",
        "Colombia",
        "Ecuador",
        "Guyana",
        "Paraguay",
        "Peru",
        "Suriname",
        "Uruguay",
        "Venezuela",
    ],
    "Europe": [
        "Albania",
        "Andorra",
        "Austria",
        "Belarus",
        "Belgium",
        "Bosnia and Herzegovina",
        "Bulgaria",
        "Croatia",
        "Cyprus",
        "Czech Republic",
        "Denmark",
        "Estonia",
        "Finland",
        "France",
        "Germany",
        "Greece",
        "Hungary",
        "Iceland",
        "Ireland",
        "Italy",
        "Kosovo",
        "Latvia",
        "Liechtenstein",
        "Lithuania",
        "Luxembourg",
        "Malta",
        "Moldova",
        "Monaco",
        "Montenegro",
        "Netherlands",
        "North Macedonia",
        "Norway",
        "Poland",
        "Portugal",
        "Romania",
        "Russia",
        "San Marino",
        "Serbia",
        "Slovakia",
        "Slovenia",
        "Spain",
        "Sweden",
        "Switzerland",
        "Ukraine",
        "United Kingdom",
        "Vatican City",
    ],
    "Asia": [
        "Afghanistan",
        "Armenia",
        "Azerbaijan",
        "Bahrain",
        "Bangladesh",
        "Bhutan",
        "Brunei",
        "Cambodia",
        "China",
        "Cyprus",
        "East Timor",
        "Georgia",
        "India",
        "Indonesia",
        "Iran",
        "Iraq",
        "Israel",
        "Japan",
        "Jordan",
        "Kazakhstan",
        "Kuwait",
        "Kyrgyzstan",
        "Laos",
        "Lebanon",
        "Malaysia",
        "Maldives",
        "Mongolia",
        "Myanmar (Burma)",
        "Nepal",
        "North Korea",
        "Oman",
        "Pakistan",
        "Palestine",
        "Philippines",
        "Qatar",
        "Saudi Arabia",
        "Singapore",
        "South Korea",
        "Sri Lanka",
        "Syria",
        "Taiwan",
        "Tajikistan",
        "Thailand",
        "Turkey",
        "Turkmenistan",
        "United Arab Emirates",
        "Uzbekistan",
        "Vietnam",
        "Yemen",
    ],
    "Africa": [
        "Algeria",
        "Angola",
        "Benin",
        "Botswana",
        "Burkina Faso",
        "Burundi",
        "Cabo Verde",
        "Cameroon",
        "Central African Republic",
        "Chad",
        "Comoros",
        "Democratic Republic of the Congo",
        "Djibouti",
        "Egypt",
        "Equatorial Guinea",
        "Eritrea",
        "Eswatini",
        "Ethiopia",
        "Gabon",
        "Gambia",
        "Ghana",
        "Guinea",
        "Guinea-Bissau",
        "Ivory Coast",
        "Kenya",
        "Lesotho",
        "Liberia",
        "Libya",
        "Madagascar",
        "Malawi",
        "Mali",
        "Mauritania",
        "Mauritius",
        "Morocco",
        "Mozambique",
        "Namibia",
        "Niger",
        "Nigeria",
        "Republic of the Congo",
        "Rwanda",
        "São Tomé and Príncipe",
        "Senegal",
        "Seychelles",
        "Sierra Leone",
        "Somalia",
        "South Africa",
        "South Sudan",
        "Sudan",
        "Tanzania",
        "Togo",
        "Tunisia",
        "Uganda",
        "Zambia",
        "Zimbabwe",
    ],
    "Australasia": [
        "Australia",
        "Fiji",
        "Kiribati",
        "Marshall Islands",
        "Micronesia",
        "Nauru",
        "New Caledonia",
        "New Zealand",
        "Palau",
        "Papua New Guinea",
        "Samoa",
        "Solomon Islands",
        "Tonga",
        "Tuvalu",
        "Vanuatu",
    ],
}


# ========The beginning of the class==========\
#  Define class shoe.
class Shoe:
    # Constructor Method.
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Return the cost of the shoe in method.
    def get_cost(self):
        return self.cost

    # Return the quantity of the shoes.
    def get_quantity(self):
        return self.quantity

    # returns a string representation of a class.
    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"


# =============Shoe list===========
# Stores  list of objects of shoes.
shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data():
    """
    Reads data of shoes from "inventory.txt" file.

    Function Description:
        This function will open the file inventory.txt
        and read the data from this file, then create a shoes object
        with this data and append this object into the shoes list. One
        line in this file represents data to create one object of shoes.
        This function will use the try-except in this function for error
        handling.

    Args:
        None

    Returns:
        None
    """
    shoe_list = []  # Initialize shoe_list

    try:
        with open("inventory.txt", "r", encoding="utf-8") as file:
            print("File opened successfully")
            file.readline()  # Skip the header line
            print("Header line skipped")
            for line in file:
                print(line.strip())
                temp = line.strip().split(",")
                shoe_list.append(
                    Shoe(temp[0], temp[1], temp[2], float(temp[3]), int(temp[4]))
                )
                print(shoe_list[-1])  # Print the last shoe added to the list
        shoe_list.sort(key=lambda x: x.quantity)  # Sort the shoe_list by quantity
        print("Shoe list sorted by quantity")
        return shoe_list  # Return the shoe_list
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        error_message = f"Error: {e}"
        print(error_message)
        with open("error_log.txt", "a", encoding="utf-8") as error_file:
            error_file.write(error_message + "\n")

            file.close()
            error_file.close()


def capture_shoes():
    """
    Request user to capture data to create shoe object.

    Function Description:
        This function will allow a user to capture data
        about a shoe and use this data to create a shoe object
        and append this object inside the shoe list.

    Args:
        None

    Returns:
        None

    """
    print(
        "Here are all continents: Africa, Australasia, Europe, North America, South America"
    )
    print("Would you like to see a list of acceptable country inputs? (y/n)")
    answer = input()
    # If user answer == "y" print list of countries in continent.
    if answer == "y":
        print("Which continent are you from? - Enter the continent: ")
        continent = input()
        if continent not in continents:
            print("Invalid continent. Please enter a valid continent: ")
            return answer

    # Request inputs to create a new shoe object
    country = input("Enter the country: ")
    # While loop continues as long as the any() function returns False
    while not any(country in countries for countries in continents.values()):
        print("Invalid country. Please enter a valid country: ")
        country = input("Enter the country: ")

    # Initialize code to an empty string
    code = ""
    # Infinite loop until the user provides a unique code.
    while True:
        code = input("Enter the code: ")
        with open("inventory.txt", "r") as file:
            for line in file:
                if code in line:
                    print("Code already exists. Please enter a new code.")
                    break
            else:
                break

    product = input("Enter the product: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    with open("inventory.txt", "a") as shoe_file_addition:
        shoe_file_addition.write(f"\n{country},{code},{product},{cost},{quantity}")
    print("Shoe data added successfully.")
    return shoe_file_addition


def delete_shoe():
    """
    Request user to give shoe code and deletes shoe from the list.

    Function Description:
        This function will allow a user to delete a shoe
        from the list based on the code of the shoe.

    Args:
        None

    Returns:
        None
    """
    # Reads data from "inventory.txt" file, stores in shoe_list.
    shoe_list = read_shoes_data()

    # Infinite loop until the user provides a valid code.
    while True:
        code = input("Enter the code of the shoe you want to delete: ")
        # Check if the provided code exists in the "inventory.txt" file.
        if any(shoe.code == code for shoe in shoe_list) and code != "":
            break
        else:
            print("Invalid code. Please enter a valid code.")

    # Search for the shoe with the provided code in the shoe list.
    for shoe in shoe_list:
        # If code exists, remove from list of shoe objects.
        if shoe.code == code:
            shoe_list.remove(shoe)
            print("Shoe deleted successfully")
            break
    else:
        print("Shoe not found")

    # Write the updated shoe list back to the "inventory.txt" file.
    with open("inventory.txt", "r+", encoding="utf-8") as file:
        file.seek(0)
        for shoe in shoe_list:
            # Write each shoe's information to the file.
            file.write(
                f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
            )
        file.truncate()

    # Ensure proper closure of the file.
    file.close()


def update_shoe():
    """
    Allows user to update the details of a shoe in the inventory.

    Function Description:
        This function allows the user to update the details (product,
        cost, and quantity) of a shoe in the inventory.

    Args:
        None

    Returns:
        None
    """
    shoe_list = read_shoes_data()

    code = input("Enter the code of the shoe you want to update: ")
    found = False

    # Iterate over the shoe list to find the shoe with the provided code.
    for shoe in shoe_list:
        if shoe.code == code:
            found = True
            # Prompt the user to update the details.
            print(f"Current details of shoe {shoe.code}:")
            print(shoe)
            print("Enter the new details:")
            product = input("Product: ")
            cost = float(input("Cost: "))
            quantity = int(input("Quantity: "))
            # Update the shoe details.
            shoe.product = product
            shoe.cost = cost
            shoe.quantity = quantity
            print("Shoe details updated successfully.")
            break

    if not found:
        print("Shoe not found.")

    # Write the updated shoe list back to the "inventory.txt" file.
    with open("inventory.txt", "w", encoding="utf-8") as file:
        for shoe in shoe_list:
            # Write each shoe's information to the file.
            file.write(
                f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
            )
        file.truncate()

    # Ensure proper closure of the file.
    file.close()


def view_all():
    """
    Reads all shoes in the inventory and prints them.

    Function Description:
        This function will iterate over the shoes list and print the
        details of the shoes returned from the __str__ function.

    Args:
        None

    Returns:
        None
    """
    # Opens  "inventory.txt" file reads  data then creates Shoe object.
    read_shoes_data()
    # For loop iterates over shoe_list and prints details of each shoe.
    for shoe in shoe_list:
        if shoe.country and shoe.code and shoe.product and shoe.cost and shoe.quantity:
            print(shoe)
            print("\n")


def re_stock():
    """
    Identifies shoe with lowest quantity and re-stocks through the user.

    Function Description:
        This function finds the shoe object with the lowest quantity,
        which is the shoes that need to be re-stocked. Ask the user if
        they want to add this quantity of shoes and then update it. This
        quantity should be updated on the file for this shoe.

    Args:
        None

    Returns:
        None
    """
    # Reads data from "inventory.txt" file, stores in shoe_list.
    read_shoes_data()
    # With statement, code creates list shoe_list to store Shoe object.
    with open("inventory.txt", "r+", encoding="utf-8") as file:
        shoe_list = []
        for line in file:
            # Skip empty lines or lines that don't contain enough information
            if not line.strip() or len(line.strip().split(",")) != 5:
                continue
            # Splits line into a list of values.
            temp = line.strip().split(",")
            # Creates a Shoe object using values.
            # Shoe object is then appended to the shoe_list.
            shoe_list.append(Shoe(temp[0], temp[1], temp[2], temp[3], temp[4]))

        if not shoe_list:
            print("Inventory file is empty or contains no valid shoe information.")
            return
        # Sorts shoe_list in ascending order by quantity.
        shoe_list.sort(key=lambda x: (x.quantity))
        # Selects the first shoe in the list.
        shoe = shoe_list[0]
        print(
            f"The shoe with the lowest quantity is {shoe.product} with a quantity of {shoe.quantity}."
        )
        answer = input("Do you want to re-stock this shoe? (y/n) ")
        if answer == "y":
            quantity = int(input("Enter the quantity you want to add: "))

            with open("inventory.txt", "r") as file:
                # Returns list of strings, each string is a line from the file.
                lines = file.readlines()
            with open("inventory.txt", "w") as file:
                # Iterates over the lines in the "inventory.txt" file.
                # For each line, checks if the line starts with the country.
                for line in lines:
                    if line.startswith(
                        f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost}"
                    ):
                        # Updates quantity of the shoe by adding the quantity.
                        new_quantity = int(line.split(",")[-1]) + quantity
                        file.write(
                            f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{new_quantity}\n"
                        )
                    else:
                        file.write(line)

        file.close()


def search_shoe():
    pass
    """
    Ask user for code of the shoe they want to search for.

    Function Description:
        This function will search for a shoe from the list
        using the shoe code and return this object so that it will be 
        printed.
        
    Args:
        None

    Returns:
        None
    """
    with open("inventory.txt", "r+", encoding="utf-8") as file:
        shoe_list = []
        for line in file:
            # Skip empty lines or lines that don't contain enough info.
            if not line.strip() or len(line.strip().split(",")) != 5:
                continue
            # Splits line into a list of values.
            temp = line.strip().split(",")
            # Shoe object is then appended to the shoe_list
            shoe_list.append(Shoe(temp[0], temp[1], temp[2], temp[3], temp[4]))

        code = input("Enter the code of the shoe you want to search for: ")
        print("\n")
        # Iterates over shoe_list, checks if code of shoe matches code.
        # user entered.
        for shoe in shoe_list:
            if shoe.code == code:
                print(shoe)
                break
        else:
            print("Shoe not found")

            file.close()


def value_per_item():
    """
    Calculates the value of each item in the inventory.

    Function Description:
        This function will calculate the total value for each item.
        Please keep the formula for value in mind: value = cost *
        quantity. Prints the value of each item on information on the
        console for all the shoes in the inventory.

    Args:
        None

    Returns:
        None
    """
    with open("inventory.txt", "r", encoding="utf-8") as file:
        shoe_list = []
        # Flag to indicate if the header line has been skipped.
        header_skipped = False
        for line in file:
            # Skip the header line.
            if not header_skipped:
                header_skipped = True
                continue
            # Skip empty lines or lines that don't contain enough information.
            if not line.strip() or len(line.strip().split(",")) != 5:
                continue
            temp = line.strip().split(",")
            # Convert cost and quantity to floats and integers.
            cost = float(temp[3])
            quantity = int(temp[4])
            shoe_list.append(Shoe(temp[0], temp[1], temp[2], cost, quantity))

            print("Value per item: ".center(50))

    # Print the total value for each item.
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print("_" * 79)
        print(f"The value of {shoe.product} is {value}.")
        print("_" * 79)
        file.close()


def highest_qty():
    """
    Code outputs shoe object with highest quantity.

    Function Description:
    This function will write code to determine the product with the
    highest quantity and print this shoe as being for sale.

    Args:
        None

    Returns:
        None
    """
    with open("inventory.txt", "r+", encoding="utf-8") as file:
        shoe_list = []
        # Flag to indicate if the header line has been skipped.
        header_skipped = False
        for line in file:
            # Skip the header line.
            if not header_skipped:
                header_skipped = True
                continue
            # Skip empty lines or lines that don't contain enough info.
            if not line.strip() or len(line.strip().split(",")) != 5:
                continue
            temp = line.strip().split(",")
            # Convert quantity to integer.
            quantity = int(temp[4])
            shoe_list.append(Shoe(temp[0], temp[1], temp[2], temp[3], quantity))

        if not shoe_list:
            print("Inventory file is empty or contains no valid shoe information.")
            return

    # Find the product with the highest quantity.
    highest_quantity = 0
    highest_product = None
    #  Iterates over the shoe_list
    # Checks if quantity of current shoe is > than  highest quantity
    for shoe in shoe_list:
        if shoe.quantity > highest_quantity:
            highest_quantity = shoe.quantity
            highest_product = shoe.product

    if highest_product:
        print(
            f"The product with the highest quantity ({highest_quantity}) is {highest_product}."
        )
    else:
        print("No product found in inventory.")

        file.close()


def country(shoe_list, continents):
    """
    Prints all shoes from a continent and total quantity of shoes within
    that continent.

    Function Description:
        This function asks the user to enter a continent and then
        prints all the shoes in the inventory that are from that
        continent.

    Args:
        shoe_list (list): A list of Shoe objects.
        continents (dict): A dictionary of continents and their
        corresponding countries.

    Returns:
        None
    """
    print(
        "Here are all continents: Africa, Australasia, Europe, North America, South America"
    )
    print("\n")
    # Get the continent from the user.
    continent = input("Enter a continent: ")
    if continent not in continents:
        print("Invalid continent")
        return

    # Get all the countries in the selected continent
    countries = continents[continent]

    # Find shoes in "inventory.txt" that are from selected countries.
    shoes_in_continent = []
    with open("inventory.txt", "r") as inventory_file:
        # Flag to indicate if the header line has been skipped.
        header_skipped = False
        for line in inventory_file:
            # Skip the header line.
            if not header_skipped:
                header_skipped = True
                continue
            # Skip empty lines or lines that don't contain enough info.
            if not line.strip() or len(line.strip().split(",")) != 5:
                continue
            country, _, _, _, _ = line.split(",")
            if country in countries:
                #  Append the entire line to the list.
                shoes_in_continent.append(line)

    # Print the shoes in the selected continent.
    if shoes_in_continent:
        print("Shoes in", continent, ":")
        print("_" * 79)
        print()
        for shoe in shoes_in_continent:
            print(shoe)
    else:
        print("No shoes in", continent)

    # Calculate the total quantity of shoes in the selected continent.
    total_quantity = 0
    # iterates over shoes_in_continent list, contains all shoes in.
    # inventory that are from the specified continent.
    for line in shoes_in_continent:
        # Splits the line into a list of values.
        _, _, _, _, quantity = line.split(",")
        # Adds quantity of the shoe to the total_quantity variable.
        total_quantity += int(quantity)

    answer = input(
        "Do you want to know the total quantity of shoes in {}? (y/n) ".format(
            continent
        )
    )
    if answer == "y":
        print(f"Total quantity of shoes in {continent} is {total_quantity}")
    else:
        print("Goodbye!")


def clear_screen():
    """
    Clears the terminal screen after 0.1 seconds.

    Function description:
        Clears the terminal screen using os.system() function.

    Args:
        None


    Returns:
        None
    """
    time.sleep(0.1)
    os.system("cls" if os.name == "nt" else "clear")

    # Main Menu loop starts here...


# ==========Main Menu=============

# While true loop that prints menu and performs functions.
while True:
    print("_" * 79)
    print("\n")
    print("Choose action you wish to excecute:".center(50, "-"))
    print("\n")
    print(
        """
                 
                 1- Open Shoe Inventory data
                 2- Add Shoe to Inventory
                 3- Delete Shoe from Inventory
                 4- View all
                 5- Re-stock Inventory Options
                 6- Search for Shoe
                 7- VPI [Value per item]
                 8- Highest Quantity
                 9- Contienents Inventory
                 10 - Update Shoe
                 11- Exit
                  
                 """.center(
            50, "-"
        )
    )
    print("\n")

    menu = input("Enter your choice: ")
    if menu == "1":
        read_shoes_data()
    elif menu == "2":
        capture_shoes()
    elif menu == "3":
        delete_shoe()
    elif menu == "4":
        view_all()
    elif menu == "5":
        re_stock()
    elif menu == "6":
        search_shoe()
    elif menu == "7":
        value_per_item()
    elif menu == "8":
        highest_qty()
    elif menu == "9":
        country(shoe_list, continents)
    elif menu == "10":
        update_shoe()
    elif menu == "11":
        print("Thank you for using Shoe Inventory!!!")
        break
    else:
        print("Invalid input")

    print()
    print("_" * 79)

    input("Press Enter to continue")
    print("..................!!!LOADING!!!..................")

    clear_screen()
    print()
