# Receipt Divider

**Receipt Divider** is a tool for splitting costs amongst a number of people. It takes data from receipts in the form of a structured file, which indicates the price of an item as well as the people which purchased that item. The program can collect this information and will output a single set of transactions that, when completed, will consolidate any owed money.

# Setup & Usage

1. Clone the repo to your local machine.
2. Create a new folder at the repo location called "receipts". This is the default location that the program will look for receipt files. This location can be changed by modifying the `dataLocation` variable.
3. Create at least one receipt file. The syntax for this is in the `File Syntax` section.
4. Run the program.

## File Syntax