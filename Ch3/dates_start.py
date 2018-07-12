#
# Example file for working with date information
#
import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = datetime.date.today()
  print ("Todays date is ", today)

  # print out the date's individual components
  print (today.day)
  # print (today.date)
  print (today.month)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print(today.weekday())
  days = ["mon", "tue", "wed", "thur", "frid"]
  print ("the day of the week is " +  days[today.weekday()])
  ## DATETIME OBJECTS
  # Get today's date from the datetime class


  # Get the current time


  
if __name__ == "__main__":
  main();
  