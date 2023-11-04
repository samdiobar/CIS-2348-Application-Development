class ItemToPurchase:

  def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
    self.item_name = item_name
    self.item_price = item_price
    self.item_quantity = item_quantity

  def print_item_cost(self):
    print('{0} {1} @ ${2:g} = ${3:g}'.format(self.item_name, self.item_quantity, self.item_price, (self.item_quantity*self.item_price)))

if __name__ == "__main__":
  items = []
  num_of_items = 2
  total = 0
  for i in range(0, num_of_items):
    new_item = ItemToPurchase()
    print("Item " + str(i+1))
    new_item.item_name = str(input("Enter the item name:\n"))
    new_item.item_price = float(input("Enter the item price:\n"))
    new_item.item_quantity = int(input("Enter the item quantity:\n"))
    print()

    items.append(new_item)
    total += new_item.item_quantity * new_item.item_price
  
  print("TOTAL COST")
  items[0].print_item_cost()
  items[1].print_item_cost()
  print()
  print("Total: ${0:g}".format(total))