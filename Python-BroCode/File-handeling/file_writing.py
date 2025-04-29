# Python file writing (.txt , .json , .csv)

import os, json, csv


csv_data = [
    ["name", "age", "phone", "adress"],
    ["XYZ", 33, "+880171XXXXX", "123 Fake street"],
    ["ABC", 45, "+88017XXXXXX", "UNA 32"],
    ["Karen", 43, "+423213313", "K. street"],
] 


json_data = {
    "name" : "XYZ",
    "age" : 33,
    "phone" : "+88017XXXXXXX",
    "adress" : "123 Fake street"
}


list_data = ["This is a", "List of",
            "some words ", "that I'm jsut testing",
            "This is a list"]


txt_data = "It's me writing somthing in Pytho_file_writing"



file_path_txt = "Stuff/test.txt"

file_path_csv = "Stuff/test.csv"

file_path_json = "Stuff/test.json"

file_path = "D:\\Study\\Python\\test_1.txt"




with open(file=file_path_csv, mode="w", newline="") as file:
   
    writer = csv.writer(file)
    for row in csv_data:
        writer.writerow(row)
    print(" .csv file successful")



with open(file=file_path_json, mode="w") as file:

    json.dump(json_data, file, indent=4)
    
    print(" .json file successful")



with open(file=file_path_txt, mode="w") as file:

    for data in list_data:
        file.write(data + "\n")

    print(".txt successful")



if os.path.exists(file_path):
    
    with open(file=file_path, mode="a") as file:

        for count in range(1, 101):
            file.write(txt_data + f" #{str(count)}\n")
        
        print("Loop writing Successful !")
else:
    print("File don't exists !") 