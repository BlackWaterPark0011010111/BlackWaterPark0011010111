import csv
from io import StringIO

# Simulate CSV data as a string
data = "Name,Age,City, John,25,New York, Alice,30,San Francisco, Bob,22,Los Angeles"

# Using StringIO to treat the CSV data string as a file-like object
with StringIO(data) as stream:
    # Creating a csv.reader object by passing the file-like object
    reader = csv.reader(stream)

    # Iterate through rows in the CSV
    for row in reader:
        print(row)


print("The contents of data: ", data)
