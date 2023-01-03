import sys
from tabulate import tabulate
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments.")

elif len(sys.argv) > 2:
    sys.exit("Not enough command-line arguments.")

elif (sys.argv[1]).endswith(".csv") == False:
    sys.exit("Not a csv file.")

else:
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file, delimiter = ",")

            tables = []
            for row in reader:
                tables.append(row)

            table = tabulate(tables, headers="firstrow", tablefmt="grid")
            print(table)
    except FileNotFoundError:
        sys.exit("File does not exist.")