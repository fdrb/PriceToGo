# PriceToGo


< Compare product prices from grocery stores using a Python based tool that integrates with an SQL database. The database was created using data from 3 grocery stores near UBC (Save-On-Foods, No Frills and Urban Fare) with the goal of enabling students to find the cheaptest prices as easily as possible. >

![image](https://github.com/user-attachments/assets/3173fe45-584e-4624-aac9-ad9d85064a39)


![]()

**Table of Contents**

- [Installation](#installation)
- [Execution / Usage](#execution--usage)
- [Technologies](#technologies)
- [Features](#features)
- [Authors](#author)
- [Change log](#change-log)

## Installation

Ensure you have the following installed:
- Python 3
- sqlite3

Database Setup
- If you have a CSV file with grocery data, load it into the SQLite database by uncommenting the following line in the script and replace filename.csv with the name of your file:

```sh
if __name__ == '__main__':
    # add_data('PriceToGo.csv', 'PriceToGo.db')
    main('PriceToGo.db')
```

Or, use the provided database file (PriceToGo.db) for testing.


## Execution / Usage

To run < PriceToGo >, fire up a terminal window and execute:

```sh
<PriceToGo.py>
```

Interactive Menu Options:
1. Compare prices of a product across stores:
    - Enter the product name to see its prices in different stores
    - Sort prices in ascending (asc) or descending (desc) order
2. Compare prices of products within a store by cateogory
    - Enter the store name and product category to view all the items in that category
    - Sort prices in ascending (asc) or descending (desc) order
3. Display all prices within a store
    - Enter the store name to display all its products and corresponding prices
    - Sort prices in ascending (asc) or descending (desc) order
4. Exit
    - Exit the program

## Technologies

< PriceToGo > uses the following technologies and tools:

- [Python](https://www.python.org/): ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- [SQLite](https://sqlite.org/): ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## Features

< PriceToGo > currently has the following set of features:

- Database Management: Automatically creates and manages an SQLite database
- Imports Data: imports product data from a CSV file
- Price Comparison:
  - Compares prices of a specific product across multiple stores
  - Compares prices within a single store by product category
  - Displays all prices and products within a single store
- Sorting: Allows sorting of results by price in ascending or descending order
- Interactive Menu: Has a simple command-line interface


## Authors

Here's the list of people who have contributed to < PriceToGo >:

- Ang Li 
- Fiona de Romer-Brisland 
- Hannah D'Souza


## Change log

- 0.0.2
    - Added sorting option (ascending and descending order) for query results
    - Improved error handling, added error message for empty queries
- 0.0.1
    - Core functionality: database management, CSV import and price comparison
