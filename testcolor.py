from tabulate import tabulate
from colorama import init, Fore, Style

# Initialize colorama
init()

# Sample data
data = [
    ["Leerling 1", 8, 7, 9],
    ["Leerling 2", 4, 5, 6],
    ["Leerling 3", 10, 9, 10],
]

# Apply color formatting to the data
for i in range(len(data)):
    for j in range(1, len(data[i])):  # Skip the name column
        if data[i][j] < 5:
            data[i][j] = f"{Fore.RED}{data[i][j]}{Style.RESET_ALL}"
        else:
            data[i][j] = f"{data[i][j]}"

# Create table with tabulate
headers = ["Naam", "Wiskunde", "Nederlands", "Geschiedenis"]
table = tabulate(data, headers, tablefmt="grid")

# Print the table
print(table)
