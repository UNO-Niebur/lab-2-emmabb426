#FutureTime.py
#Name: Emma Barnes
#Date: 01/30/2026
#Assignment: Lab 02 - Future Time

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour -6) % 24
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  hours = int(input("How many hours do you want to add to the current time? "))
  #Ask user for minutes
  minutes = int(input("How many minutes do you want to add to the current time? "))
  #Calculate the time after the user-supplied time has passed.
  futureMins = (currentMinute + minutes) % 60
  extraHour = (currentMinute + minutes) // 60
  futureHour = (currentHour + hours) % 24 
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  HH = (futureHour + extraHour) % 24
  mins = futureMins
  print(f"The time will be: {HH}:{mins}")

if __name__ == '__main__':
  main()
