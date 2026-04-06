from database import create_connection, initialize_db, add_item, get_items, update_item_quantity, get_item_by_id
from models import Item

def print_items(items):
    
    for item in items:
        print(f'ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Price: {item[3]}')

def main_menu(conn):
    
    while True:
        print("\n--- Inventory Management System ---")
        print("1. View all items")
        print("2. Add new item")
        print("3. Buy item")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            items = get_items(conn)
            print_items(items)
        elif choice == '2':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            add_item(conn, name, quantity, price)
            print("Item added successfully.")
        elif choice == '3':
            item_id = int(input("Enter item ID to buy: "))
            quantity = int(input("Enter quantity to buy: "))
            item = get_item_by_id(conn, item_id)
            if item:
                if item[2] >= quantity:
                    update_item_quantity(conn, item_id, quantity)
                    print("Purchase successful.")
                else:
                    print("Not enough stock available.")
            else:
                print("Item not found.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
