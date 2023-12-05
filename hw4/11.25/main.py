# Name: Samuel Barroso
# PSID: 1844307

if __name__ == "__main__":
    # FIXME (1): Prompt for four weights. Add all weights to a list. Output list.
    weights = []
    for i in range(0,4):
        response = float(input(f'Enter weight {i+1}:\n'))
        weights.append(response)
    print(f'Weights: {weights}\n')

    # FIXME (2): Output average of weights.
    average = sum(weights) / len(weights)
    print("Average weight: " + ("%.2f" % average))
    
    # FIXME (3): Output max weight from list.
    print("Max weight: " + ("%.2f" % max(weights)) + "\n")
    
    # FIXME (4): Prompt the user for a list index and output that weight in pounds and kilograms.
    index = int(input("Enter a list location (1 - 4):\n")) - 1
    in_kilos = weights[index] / 2.2
    print("Weight in pounds: " + ("%.2f" % weights[index]))
    print("Weight in kilograms: " + ("%.2f" % in_kilos) + "\n")
    
    # FIXME (5): Sort the list and output it.
    weights.sort()
    print(f'Sorted list: {weights}')