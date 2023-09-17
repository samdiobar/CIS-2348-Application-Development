# Samuel Barroso 1844307
print("Enter amount of lemon juice (in cups):")
juice = float(input())
print("Enter amount of water (in cups):")
water = float(input())
print("Enter amount of agave nectar (in cups):")
nectar = float(input())
print("How many servings does this make?")
servings = float(input())
print()

print("Lemonade ingredients - yields", '{:.2f}'.format(servings), "servings")
print('{:.2f}'.format(juice), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(nectar), "cup(s) agave nectar")

print()
print("How many servings would you like to make?")
servings_desired = float(input())
print()

print("Lemonade ingredients - yields", '{:.2f}'.format(servings_desired), "servings")
scale = servings_desired / servings
print('{:.2f}'.format(juice * scale), "cup(s) lemon juice")
print('{:.2f}'.format(water * scale), "cup(s) water")
print('{:.2f}'.format(nectar * scale), "cup(s) agave nectar")

print()

print("Lemonade ingredients - yields", '{:.2f}'.format(servings_desired), "servings")
print('{:.2f}'.format(juice * scale / 16), "gallon(s) lemon juice")
print('{:.2f}'.format(water * scale / 16), "gallon(s) water")
print('{:.2f}'.format(nectar * scale / 16), "gallon(s) agave nectar")