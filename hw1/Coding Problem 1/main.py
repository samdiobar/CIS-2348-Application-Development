# Samuel Barroso 1844307
import math

print("Enter current day:")
cur_day = int(input())
print("Enter current month:")
cur_month = int(input())
print("Enter current year:")
cur_year = int(input())

print("Enter birth day:")
birth_day = int(input())
print("Enter birth month:")
birth_month = int(input())
print("Enter birth year:")
birth_year = int(input())

age = 0
if cur_month > birth_month:
    age = cur_year - birth_year
elif cur_month == birth_month and cur_day >= birth_day:
    age = cur_year - birth_year
else:
    age = cur_year - birth_year - 1
is_birthday = False
if cur_month == birth_month and cur_day == birth_day:
    is_birthday = True

print("Birthday Calculator")
print("Current day")
print("Month:", cur_month)
print("Day:", cur_day)
print("Year:", cur_year)
print("Birthday")
print("Month:", birth_month)
print("Day:", birth_day)
print("Year:", birth_year)
print("You are", age, "years old.")
if is_birthday: print("Happy Birthday!")