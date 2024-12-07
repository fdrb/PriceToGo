# PriceToGo


< Compare product prices from grocery stores using a Python based tool that integrates with an SQL database >

< Add an optional screenshot of your project below >

![]()

**Table of Contents**

- [Installation](#installation)
- [Execution / Usage](#execution--usage)
- [Technologies](#technologies)
- [Features](#features)
- [Authors](#author)
- [Change log](#change-log)

## Installation

On macOS and Linux:

```sh
$ python -m pip install <project-name>
```

On Windows:

```sh
PS> python -m pip install <project-name>
```

## Execution / Usage

To run < PriceToGo >, fire up a terminal window and run the following command:

```sh
$ <project>
```

Here are a few examples of using the < project's name > library in your code:

```python
from project import Project

...
```

For more examples, please refer to the project's [Wiki](wiki) or [documentation page](docs).

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
