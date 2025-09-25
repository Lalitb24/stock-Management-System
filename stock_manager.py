import json
import os

# File to store stock data
DATA_FILE = 'stock_data.json'

def load_stock():
    """Load stock data from JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_stock(stock):
    """Save stock data to JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(stock, f, indent=4)

def add_item(stock):
    """Add a new item to stock."""
    name = input("Enter item name: ").strip()
    if name in stock:
        print("Item already exists. Use update to add quantity.")
        return
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
        stock[name] = {'quantity': quantity, 'price': price}
        save_stock(stock)
        print(f"Added {name}: {quantity} units at ${price} each.")
    except ValueError:
        print("Invalid input. Quantity must be integer, price must be number.")

def view_stock(stock):
    """View all stock items."""
    if not stock:
        print("No items in stock.")
        return
    print("\n--- Current Stock ---")
    total_value = 0
    for name, details in stock.items():
        value = details['quantity'] * details['price']
        total_value += value
        print(f"{name}: {details['quantity']} units @ ${details['price']:.2f} = ${value:.2f}")
    print(f"Total stock value: ${total_value:.2f}")

def update_quantity(stock):
    """Update quantity of an item (add or remove)."""
    name = input("Enter item name: ").strip()
    if name not in stock:
        print("Item not found.")
        return
    try:
        change = int(input("Enter quantity change (+ to add, - to remove): "))
        stock[name]['quantity'] += change
        if stock[name]['quantity'] <= 0:
            del stock[name]
            print(f"Removed {name} (quantity reached zero).")
        else:
            save_stock(stock)
            print(f"Updated {name}: new quantity = {stock[name]['quantity']}")
    except ValueError:
        print("Invalid input.")

def search_item(stock):
    """Search for an item."""
    name = input("Enter item name to search: ").strip().lower()
    found = False
    for key in stock:
        if name in key.lower():
            details = stock[key]
            value = details['quantity'] * details['price']
            print(f"{key}: {details['quantity']} units @ ${details['price']:.2f} = ${value:.2f}")
            found = True
    if not found:
        print("No matching items found.")

def delete_item(stock):
    """Delete an item from stock."""
    name = input("Enter item name to delete: ").strip()
    if name in stock:
        del stock[name]
        save_stock(stock)
        print(f"Deleted {name}.")
    else:
        print("Item not found.")

def main():
    """Main menu loop."""
    stock = load_stock()
    while True:
        print("\n--- Stock Management System ---")
        print("1. Add item")
        print("2. View stock")
        print("3. Update quantity")
        print("4. Search item")
        print("5. Delete item")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            add_item(stock)
        elif choice == '2':
            view_stock(stock)
        elif choice == '3':
            update_quantity(stock)
        elif choice == '4':
            search_item(stock)
        elif choice == '5':
            delete_item(stock)
        elif choice == '6':
            save_stock(stock)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
