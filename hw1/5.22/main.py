# Samuel Barroso 1844307
import math

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print()

print("Select first service:")
service1 = str(input())
print("Select second service:")
service2 = str(input())

services = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12,
    "-": 0
}
print()

print("Davy's auto shop invoice")
print()
if service1 != "-":
    print("Service 1:", service1 + ", $" + str(services[service1]))
else:
    print("Service 1: No service")
if service2 != "-":
    print("Service 2:", service2 + ", $" + str(services[service2]))
else:
    print("Service 2: No service")
print()
print("Total: $" + str(services[service1] + services[service2]))
