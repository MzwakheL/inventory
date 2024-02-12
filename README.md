# Shoe Inventory Management System

# Description
The Shoe Inventory Management System is a Python script designed to assist in the management of shoe inventory. It allows users to perform various operations such as adding new shoes, viewing all shoes, restocking low quantity shoes, searching for specific shoes, calculating the value per item, and finding the product with the highest quantity. The system offers functionalities to efficiently manage inventory data and streamline inventory-related tasks.

# Features
Shoe Addition: Users can add new shoe entries, including details such as country, code, product, cost, and quantity.
Shoe Viewing: Users can view all existing shoe entries, displaying comprehensive information for each shoe, organized in tabular format.
Shoe Restocking: The system identifies shoes with low quantities and prompts users to restock them, updating the inventory accordingly.
Shoe Searching: Users can search for specific shoes by entering the shoe code, enabling quick access to relevant information.
Value Calculation: The system calculates the total value for each shoe based on its cost and quantity, providing valuable insights into inventory valuation.
Highest Quantity Identification: Users can identify the product with the highest quantity in the inventory, facilitating sales and inventory management decisions.
Usage
Installation: Clone the repository or download the Python script (shoe_inventory.py) to your local machine.

Dependencies: Ensure you have Python installed on your system, along with the tabulate module. You can install the module using pip install tabulate.

Run the Script: Open a terminal or command prompt, navigate to the directory containing the script, and run the script using the command python shoe_inventory.py.

Main Menu: Upon running the script, users will be presented with a main menu where they can select various options to manage shoe inventory.

Input: Follow the on-screen instructions to perform desired operations such as adding shoes, viewing inventory, restocking shoes, searching for specific shoes, and more.

Output: The script will display relevant information based on user input, providing comprehensive insights into shoe inventory data.

# Example Usage
Adding a Shoe:

sql
Copy code
Please first press option 1 to read the shoes data then press any options

--- MENU ---
1. Read shoes data
2. Capture new shoe
3. View all shoes
4. Re-stock shoes
5. Search for a shoe
6. Calculate value per item
7. Find the product with the highest quantity
8. Exit

Enter your choice (1-8): 2

Please enter a country: USA
Please enter a code: SH123
Please enter product: Running Shoes
Enter cost: 49.99
Enter quantity: 100

Shoe added.
Viewing All Shoes:

sql
Copy code
Please first press option 1 to read the shoes data then press any options

--- MENU ---
1. Read shoes data
2. Capture new shoe
3. View all shoes
4. Re-stock shoes
5. Search for a shoe
6. Calculate value per item
7. Find the product with the highest quantity
8. Exit

Enter your choice (1-8): 3
+---------+-------+----------------+--------+----------+
| Country | Code  | Product        |  Cost  | Quantity |
+---------+-------+----------------+--------+----------+
|   USA   | SH123 | Running Shoes  | 49.99  |   100    |
|   UK    | SH456 | Sports Sneaker | 39.99  |    50    |
|   USA   | SH789 | Casual Shoes   | 29.99  |    75    |
+---------+-------+----------------+--------+----------+
