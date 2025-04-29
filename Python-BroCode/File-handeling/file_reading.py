
import json, csv

# file_path = "D:\\Study\\Python\\test_1.txt"
# file_path = "Stuff/test.json"
file_path = "Stuff/test.csv"

try:
    with open(file_path ,"r") as file:
    
        # content = file.read()
    
        # content = json.load(file)

        content = csv.reader(file)
        for line in content:
            print(line)

except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You don't have the permisson to see this file")
    