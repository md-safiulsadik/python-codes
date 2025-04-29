# Old: print "The answer is", 3*3
# New: print("The answer is", 3*23)

# Old: print a,           # Trailing comma suppresses newline
# New: print(a, end=" ")  # Appends a space instead of a newline

# Old: print              # Prints a newline
# New: print()            # You must call the function!

# Old: print >>sys.stderr, "fatal error"
# New: print("fatal error", file=sys.stderr)

# Old: print (a, b)       # prints repr((a, b))
# New: print((a, b))      # Not the same as print(a, b)

print(""" 
                    Twinkle, twinkle, little star,
                            How I wonder what you are! 
                                    Up above the world so high,   		
                                    Like a diamond in the sky. 
                    Twinkle, twinkle, little star, 
                            How I wonder what you are
      """)

binary = 5.1342112645

import sys
print(sys.version)

import platform
print(platform.python_version())


import datetime
time = datetime.datetime.now()

print("Current Time :")
print(time.strftime("Time : %H:%M:%S\nDate : %d-%m-%Y"))


num = int(input("Number "))
status = "Good" if num > 80 else "LOL"
print(status)
from msvcrt import getch
getch()
