class ItemToPurchase:
  def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
    self.item_name = item_name
    self.item_price = item_price
    self.item_quantity = item_quantity
    self.item_description = item_description

  def print_item_cost(self):
    print('{0} {1} @ ${2:g} = ${3:g}'.format(self.item_name, self.item_quantity, self.item_price, (self.item_quantity*self.item_price)))

  def print_item_description(self):
    print(self.item_name + ":", self.item_description)

class ShoppingCart:
  def __init__(self, customer_name="none", current_date="January 1, 2016"):
    self.customer_name = customer_name
    self.current_date = current_date
    self.cart_items = []

  def add_item(self, ItemToPurchase):
    self.cart_items.append(ItemToPurchase)
  
  def remove_item(self, name):
    for item in self.cart_items:
      if item.item_name == name:
        self.cart_items.remove(item)
        return
    print("Item not found in cart. Nothing removed.")

  def modify_item(self, ItemToPurchase):
    name = ItemToPurchase.item_name
    for item in self.cart_items:
      if item.item_name == name:
        self.cart_items[self.cart_items.index(item)] = ItemToPurchase
        return
    print("Item not found in cart. Nothing modified.")

  def get_num_items_in_cart(self):
    return len(self.cart_items)
  
  def get_cost_of_cart(self):
    total = 0
    for item in self.cart_items:
      total += item.item_price * item.item_quantity
    return total

  def print_total(self):
    if self.get_num_items_in_cart() <= 0:
      print("SHOPPING CART IS EMPTY")
      return
    print(self.customer_name + "'s Shopping Cart - " + self.current_date)
    print("Number of Items: " + str(self.get_num_items_in_cart()) + "\n")
    for item in self.cart_items:
      item.print_item_cost()
    print()
    print("Total: $" + str(self.get_cost_of_cart()))

  def print_descriptions(self):
    if self.get_num_items_in_cart() <= 0:
      print("SHOPPING CART IS EMPTY")
      return
    print(self.customer_name + "'s Shopping Cart - " + self.current_date + "\n")
    print("Item Descriptions")
    for item in self.cart_items:
      item.print_item_description()

    pass


if __name__ == "__main__":
  customer_name = str(input("Enter customer's name:"))
  todays_date = str(input("Enter today's date:"))
  cart = ShoppingCart(customer_name, todays_date)