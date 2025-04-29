
import random
import string

char = " " + string.punctuation + string.ascii_letters + string.digits
char = list(char)
# print(char)
key = char.copy()
random.shuffle(key)
# print()
# print()
# print(key)

#encrytion
user_massage = input("Type a massage to encrypte it :  ")
encrypte_massage = ""
original = ""

for latter in user_massage:
    index = char.index(latter)
    encrypte_massage += key[index]

print() #f"Original Massage : {user_massage}")
print(f"Encrypted Massage : {encrypte_massage}")

# Decryption
for en_latter in encrypte_massage:
    index_ = key.index(en_latter)
    original += char[index_]

print()
print(f"Original Massage : {original}")

from msvcrt import getch
getch()
