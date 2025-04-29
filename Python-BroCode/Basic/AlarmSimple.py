
import time

myTime = int(3605)
for x in range(myTime , 0, -1):
    sec = x % 60
    min = int(x / 60) % 60
    hour = int(x / 3600)
    print(f"{hour:02}:{min:02}:{sec:02}")
    time.sleep(1)
print("Sound !\nWake UP !!")
print("Wake UP !")
print("Wake UP !")



# Calculating Hours, Minutes, and Seconds

# Let's break down the calculations for hours, minutes, and seconds:

# 1. Seconds: sec = x % 60

# The % operator is the modulus operator, which returns the remainder of the division of x by 60.
# This gives us the remaining seconds, because there are 60 seconds in a minute.
# For example, if x is 125, x % 60 would be 5, because 125 divided by 60 leaves a remainder of 5.
# 2. Minutes: min = int(x / 60) % 60

# First, we divide x by 60 to get the total number of minutes.
# We use the int() function to truncate the result to an integer, because we don't want any fractional minutes.
# Then, we take the result modulo 60 to get the remaining minutes.
# This is because there are 60 minutes in an hour, so if we have more than 60 minutes, we want to wrap around to the next hour.
# For example, if x is 125, int(x / 60) would be 2, because 125 divided by 60 is approximately 2.08. Then, 2 % 60 would be 2, because 2 is less than 60.
# 3. Hours: hour = int(x / 3600)

# We divide x by 3600 to get the total number of hours.
# We use the int() function to truncate the result to an integer, because we don't want any fractional hours.
# This gives us the remaining hours, because there are 3600 seconds in an hour.
# For example, if x is 125, int(x / 3600) would be 0, because 125 divided by 3600 is approximately 0.034.
# By using these calculations, we can break down the total number of seconds into hours, minutes, and seconds.