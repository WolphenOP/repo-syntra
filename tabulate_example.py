# Import the tabulate module
from tabulate import tabulate

# Sample data: list of lists
data = [
    ["Alice", 24, "Engineer"],
    ["Bob", 30, "Data Scientist"],
    ["Charlie", 28, "Teacher"]
]

# Creating a table with headers and a grid format
table = tabulate(
    data,
    headers=["Name", "Age", "Profession"],
    tablefmt="pretty"
)

print(table)