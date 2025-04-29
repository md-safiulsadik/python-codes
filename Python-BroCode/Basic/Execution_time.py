
import time

start_time = time.perf_counter()

text_data = "printing something"

file_path = "test.txt"

# with open(file=file_path , mode="w") as file:
#     for count in range(1 , 10):
#         time.sleep(1)
#         file.write(f"{text_data} #{count}\n")
#     print("successful !")

for _ in range(100000000):
    pass


end_time = time.perf_counter()

elapsed_time = end_time - start_time

print(f"Elapsed time : {elapsed_time:.01f}sec")