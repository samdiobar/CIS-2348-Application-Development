# Samuel Barroso 1844307
import math

print("Enter wall height (feet):")
height = int(input())
print("Enter wall width (feet):")
width = int(input())
area = height * width
print("Wall area:", area, "square feet")

paint_needed = area / 350
print("Paint needed:", '{:.2f}'.format(paint_needed), "gallons")
print("Cans needed:", math.ceil(paint_needed), "can(s)")
print()

colors = {
    "red": 35,
    "blue": 25,
    "green": 23
}
print("Choose a color to paint the wall:")
color = str(input())
print("Cost of purchasing", color, "paint: $" + str(math.ceil(paint_needed) * colors[color]))