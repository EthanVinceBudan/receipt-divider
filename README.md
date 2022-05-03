# Receipt Divider

**Receipt Divider** is a tool for splitting costs amongst a number of people. It takes data from receipts in the form of a structured file, which indicates the price of an item as well as the people which purchased that item. The program can collect this information and will output a single set of transactions that, when completed, will consolidate any owed money.

# Setup & Usage

1. Clone the repo to your local machine.
2. Create a new folder at the repo location called "receipts". This is the default location that the program will look for receipt files. This location can be changed by modifying the `dataLocation` variable within `main.py`.
3. Create at least one receipt file. The syntax for this is in the `File Syntax` section.
4. Run the program.

## File Syntax

For **Receipt Divider** to properly parse receipt information, it must follow the proper syntax outlined below:

- The file must begin with a `paid by: Person` statement. This indicates who originally paid for all the items outlined in the rest of the receipt file.
- Specifying an item is done using `price Person1[,Person2,..]`, where price is the total cost of the item as a decimal number, and Person1,Person2... is a comma seperated list of every person who should be paying for that item.
- All item and paid by statements must be on seperate lines.

A valid receipt file can have any extension, as long as it can be interpreted as text by Python.

### Example File

> paid by: Alice
>
> 5.99 Alice,Bob,Charles
>
> 13.99 Bob,Charles
>
> 2.99 Dylan
>
> 4.99 Alice,Dylan

generated output:

> total of receipt example.receipt = $27.96
>
> ----------------------------------
>
> Bob owes Alice : $8.99
>
> Charles owes Alice : $8.99
>
> Dylan owes Alice : $5.49