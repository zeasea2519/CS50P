import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments.")

elif len(sys.argv) > 3:
    sys.exit("Not enough command-line arguments.")

elif (sys.argv[1]).endswith(".csv") == False:
    sys.exit("Not a csv file.")

else:
    students = []
    try:
        with open(sys.argv[1]) as file1:
            reader = csv.DictReader(file1)
            for row in reader:
                last_name, first_name = row["name"].split(", ")
                house = row["house"]
                students.append({"first": first_name, "last": last_name, "house": house})

        keys = students[0].keys()
        with open(sys.argv[2], "w") as file2:
            write = csv.DictWriter(file2, keys)
            write.writeheader()
            write.writerows(students)
    except FileNotFoundError:
        sys.exit("File does not exist.")