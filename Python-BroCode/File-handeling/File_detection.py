# Python file detection

import os 

# file_path = "D:\\Tafsair\\Tafsir Ibn Kathir all 10 volumes.pdf"
file_path = "D:\\Download"

if os.path.exists(file_path):
    print("File found !")

    if os.path.isfile(file_path):
        print("It's a file !")
    
    elif os.path.isdir(file_path):
        print("It's a folder")

else:
    print("Not found !")
