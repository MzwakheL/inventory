from tabulate import tabulate
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        pass
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        return self.cost
        pass
        '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        self.quantity
        pass
        '''
        Add the code to return the quantity of the shoes.
        '''

    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"
        pass
        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    try: 
        with open('inventory.txt', 'r') as file:
            next(file)
            for line in file:
                data = line.strip().split(',')
                shoes = Shoe(data[0], data[1], data[2], float(data[3]), int(data[4]))
                shoe_list.append(shoes)
    except FileExistsError:
        print("\nFile not found.")
    pass
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
def capture_shoes():
    country = input("\nPlease enter a country: ")
    code = input("\nPlease enter a code: ")
    product = input("\nPlease enter product: ")
    cost = float(input("\nEnter cost: "))
    quantity = int(input("\nEnter quantity: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print("\nShoe added.")
    pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    if not shoe_list:
        print("\nNo shoes found.")

    else:
        headers = ["Country", "Code", "Product", "Cost", "Quantity"]
        data = [[s.country, s.code, s.product, s.cost, s.quantity] for s in shoe_list]
        print(tabulate(data, headers=headers))
    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():
    if not shoe_list:
        print("\nNo shoes found.")
    
    else:
         # find shoe with lowest quantity

        lowest_qty = float('inf')
        for s in shoe_list:
            if s.quantity < lowest_qty:
                lowest_qty = s.quantity
                shoe = s

        # ask user to restock

        print(f"Shoe with code {shoe.code} needs to be restocked.")
        restock_qty = int(input("Enter restock quantity: "))
        if restock_qty > 0:
            shoe.quantity += restock_qty
            print(f"{restock_qty} units added to shoe with code {shoe.code}.")

            # update file

            with open('inventory.txt', 'r') as file:
                lines = file.readlines()
            with open('inventory.txt', 'w') as file:
                file.write(lines[0]) # write header line
                for s in shoe_list:
                    if s.code == shoe.code:
                        file.write(f"{s.country},{s.code},{s.product},{s.cost},{s.quantity}\n")
                    else:
                        file.write(f"{s.country},{s.code},{s.product},{s.cost},{s.quantity}\n")

    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def seach_shoe():
    code = input("Enter shoe code to search: ")
    for s in shoe_list:
        if s.code == code:
            print(s)
            return
    print("\nShoe not found.")
    pass
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    if not shoe_list:
        print("\nNo shoes found.")

    else:
        headers = ["Code", "Value"]
        data = [[s.code, s.cost * s.quantity] for s in shoe_list]
        print(tabulate(data, headers=headers))
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    if not shoe_list:
        print("\nNo shoes found.")

    else:
        highest_qty = 0
        highest_qty_list = None
        for s in shoe_list:
            if s.quantity > highest_qty:
                highest_qty = s.quantity
                highest_qty_shoe = s
        print(f"\nShoe with highest quantity: {highest_qty_shoe}")
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

while True:
    print("\nPlease first press option 1 to read the shoes data then press any options")
    print("\n--- MENU ---")
    print("1. Read shoes data")
    print("2. Capture new shoe")
    print("3. View all shoes")
    print("4. Re-stock shoes")
    print("5. Search for a shoe")
    print("6. Calculate value per item")
    print("7. Find the product with the highest quantity")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        read_shoes_data()

    elif choice == "2":
        capture_shoes()

    elif choice == "3":
        view_all()

    elif choice == "4":
        re_stock()

    elif choice == "5":
        seach_shoe()

    elif choice == "6":
        value_per_item()

    elif choice == "7":
        highest_qty()

    elif choice == "8":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")