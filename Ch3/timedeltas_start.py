#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print (timedelta(days=365, hours = 5, minutes = 41))

# print today's date
today = datetime.now()
print (today)
#print (today.strftime(%X))


# print today's date one year from now
year_after = today + timedelta(days=365)

print (year_after)
# create a timedelta that uses more than one argument
print ("after three weeks and 2 days date will be" +str (today + timedelta(week=3, days =2))) 


# calculate the date 1 week ago, formatted as a string


### How many days until April Fools' Day?


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# Now calculate the amount of time until April Fool's Day  


