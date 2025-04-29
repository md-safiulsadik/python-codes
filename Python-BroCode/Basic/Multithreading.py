# multithreading = Used to perform multiple tasks concurrently (multitasking
#                 Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target=function_name)

import threading
import time


def cycling():
    time.sleep(6)  
    print("You return home")

def read_tafsir(key, value):
    time.sleep(4)
    print(f"You read tafsir {key} : Vol {value}")

def read_shira(name):
    time.sleep(5)
    print(f"You read shira '{name}")

chore1 =threading.Thread(target=cycling)
chore1.start()

chore2 = threading.Thread(target=read_tafsir , args=("Ibn Kathir" , 10))
chore2.start()

chore3 = threading.Thread(target=read_shira, args=["Ar Rahikul Makhutm"])
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("You are ready for work")

# cycling()
# read_tafsir()
# read_shira()