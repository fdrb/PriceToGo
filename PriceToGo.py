import sqlite3
import json
import csv

def add_data(data_fn, db_fn):
    # connect to SQLite database
    conn = sqlite3.connect(db_fn)
    c = conn.cursor()

    # Create a table to store grocery store price data
    c.execute('''CREATE TABLE IF NOT EXISTS product (
                store TEXT,
                product_category TEXT,
                product_name TEXT,
                price REAL,
                UNIQUE(store, product_name)
                )''')
    
    # Read CSV file and import data into SQLite database
    try:
        with open(data_fn, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # skip column name 
            for row in csvreader:
                # print(row)
                store, product_category, product_name, price = row
                c.execute("INSERT OR IGNORE INTO product (store, product_category, product_name, price) VALUES (?, ?, ?, ?)",
                        (store, product_category, product_name, float(price)))
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    conn.close()


# Search and compare the prices of the same product in three different grocery stores
def compare_prices_across_stores(c, product_name, order='asc'):
    # c.execute("SELECT store, price FROM product WHERE product_name=?", (product_name,))
    c.execute("SELECT store, product_name, price FROM product WHERE product_name LIKE ? ORDER BY price " + order,
              ('%' + product_name + '%',))
    return c.fetchall()


# Query and compare prices of similar products in a single grocery store (based on product category)
def compare_prices_within_store(c, store, product_category, order='asc'):
    c.execute("SELECT product_name, price FROM product WHERE store LIKE ? AND product_category LIKE ? ORDER BY price " + order,
              (store, product_category))
    return c.fetchall()


# Query and display the prices of all products in a single grocery store
def display_prices_within_store(c, store, order='asc'):
    c.execute("SELECT product_category, product_name, price FROM product WHERE store LIKE ? ORDER BY price " + order,
              (store,))
    return c.fetchall()


def main(db_fn):
    # connect to SQLite database
    conn = sqlite3.connect(db_fn)
    c = conn.cursor()
    while True:
        print("\n1. Compare prices of a product across stores")
        print("\n2. Compare prices of products within a store by category")
        print("\n3. Display all prices within a store")
        print("\n4. Exit")
        choice = input("Choose an option (1/2/3/4): ").strip()
    
        if choice == '1':
            product_name = input("Enter the product name to compare across stores: ").strip()
            order = ""
            while order not in ["asc", "desc"]:
                order = input("Sort by price (asc/desc): ").strip().lower()
                if order not in ["asc", "desc"]:
                    print("Invalid input. Please enter 'asc' for ascending or 'desc' for descending.")
            print(f"\nComparing prices of '{product_name}' across stores:")
            # for store, price in compare_prices_across_stores(product_name, order):
            #     print(f"{store}: ${price:.2f}")
            result = compare_prices_across_stores(c, product_name, order)
            if len(result) == 0:
                print("ERROR: No result founded")
            else:
                for store, product_name, price in result:
                    print(f"[{store}] : [{product_name}] : ${price:.2f}")
    
        elif choice == '2':
            store = input("Enter the store name: ").strip()
            product_category = input("Enter the product category: ").strip()
            order = ""
            while order not in ["asc", "desc"]:
                order = input("Sort by price (asc/desc): ").strip().lower()
                if order not in ["asc", "desc"]:
                    print("Invalid input. Please enter 'asc' for ascending or 'desc' for descending.")
            print(f"\nComparing prices of products in '{product_category}' category at '{store}':")
            # for product_name, price in compare_prices_within_store(store, product_category, order):
            #     print(f"{product_name}: ${price:.2f}")
            result = compare_prices_within_store(c, store, product_category, order)
            if len(result) == 0:
                print("ERROR: No result founded")
            else:
                for product_name, price in result:
                    print(f"{product_name}: ${price:.2f}")
    
        elif choice == '3':
            store = input("Enter the store name: ").strip()
            order = ""
            while order not in ["asc", "desc"]:
                order = input("Sort by price (asc/desc): ").strip().lower()
                if order not in ["asc", "desc"]:
                    print("Invalid input. Please enter 'asc' for ascending or 'desc' for descending.")
            print(f"\nDisplaying all prices at '{store}':")
            # for category, product_name, price in display_prices_within_store(store, order):
            #     print(f"{category} - {product_name}: ${price:.2f}")
            result = display_prices_within_store(c, store, order)
            if len(result) == 0:
                print("ERROR: No result founded")
            else:
                for category, product_name, price in result:
                    print(f"[{category}] : [{product_name}] : ${price:.2f}")
    
        elif choice == '4':
            break
    
        else:
            print("Invalid option. Please choose again.")
    conn.close()


if __name__ == '__main__':
    # add_data('PriceToGo.csv', 'PriceToGo.db')
    main('PriceToGo.db')
