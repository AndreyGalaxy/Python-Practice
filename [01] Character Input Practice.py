from datetime import datetime
from datetime import date

def name_code():
    while True:
        name = input("Your Name: ")
        print("Is this correct? " + name)
        while True:
            answer = input("Y/N: ")
            if answer.lower() in ["y", "yes", "n", "no"]:
              break
            else:
              print("Please enter Y/N")
              continue
        if answer.lower() in ["n", "no"]:
           continue
        else:
           return name
        
def get_age():
   while True:
    age = int(input("Your Age: "))
    if age >=0:
        return age
    else:
        print("Please enter a Valid Age")
        continue

name = name_code()
age = get_age()

Today = date.today()
year = Today.year

if age >= 100:
   print(f"{name}, you are already {age} years old! You have been 100 since {year - age + 100}!")
else:
   year_at_100 = year - age + 100
   years_until_100 = 100 - age
   print(name + ", you will turn 100 in year " + str(year_at_100) + "; " + str(years_until_100) + " years from now.")
