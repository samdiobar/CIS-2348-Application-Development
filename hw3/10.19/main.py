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
        self.cart_items[self.cart_items.index(item)].item_quantity = ItemToPurchase.item_quantity
        return
    print("Item not found in cart. Nothing modified.")

  def get_num_items_in_cart(self):
    num_of_items = 0
    for item in self.cart_items:
      num_of_items += item.item_quantity
    return num_of_items
  
  def get_cost_of_cart(self):
    total = 0
    for item in self.cart_items:
      total += item.item_price * item.item_quantity
    return total

  def print_total(self):
    print(self.customer_name + "'s Shopping Cart - " + self.current_date)
    print("Number of Items: {0}\n".format(self.get_num_items_in_cart()))
    if self.get_num_items_in_cart() <= 0:
      print("SHOPPING CART IS EMPTY")
    for item in self.cart_items:
      item.print_item_cost()
    print()
    print('Total: ${0:g}\n'.format(self.get_cost_of_cart()))

  def print_descriptions(self):
    if self.get_num_items_in_cart() <= 0:
      print("SHOPPING CART IS EMPTY")
      return
    print(self.customer_name + "'s Shopping Cart - " + self.current_date + "\n")
    print("Item Descriptions")
    for item in self.cart_items:
      item.print_item_description()


def print_menu(cart):
  user_input = ""
  while user_input != "q":
    if user_input == "o":
      print("OUTPUT SHOPPING CART")
      cart.print_total()
      user_input = ""
    elif user_input == "i":
      print("OUTPUT ITEMS' DESCRIPTIONS")
      cart.print_descriptions()
      user_input = ""
      print()
    elif user_input == "a":
      print("ADD ITEM TO CART")
      new_item = ItemToPurchase()
      new_item.item_name = str(input("Enter the item name:\n"))
      new_item.item_description = str(input("Enter the item description:\n"))
      new_item.item_price = float(input("Enter the item price:\n"))
      new_item.item_quantity = int(input("Enter the item quantity:\n"))
      cart.add_item(new_item)
      user_input = ""
      print()
    elif user_input == "r":
      print("REMOVE ITEM FROM CART")
      cart.remove_item(str(input("Enter name of item to remove:\n")))
      user_input = ""
      print()
    elif user_input == "c":
      print("CHANGE ITEM QUANTITY")
      new_item = ItemToPurchase()
      new_item.item_name = str(input("Enter the item name:\n"))
      new_item.item_quantity = int(input("Enter the new quantity:\n"))
      cart.modify_item(new_item)
      user_input = ""
      print()
    else:
      print("MENU")
      print("a - Add item to cart")
      print("r - Remove item from cart")
      print("c - Change item quantity")
      print("i - Output items' descriptions")
      print("o - Output shopping cart")
      print("q - Quit")
      print()
      user_input = str(input("Choose an option:\n"))
      while True:
        try:
          if user_input not in ["a", "r", "c", "i", "o", "q"]:
            user_input = str(input("Choose an option:\n"))
          else:
            break
        except:
          break


if __name__ == "__main__":
  customer_name = str(input("Enter customer's name:\n"))
  todays_date = str(input("Enter today's date:\n"))
  cart = ShoppingCart(customer_name, todays_date)
  print()
  print("Customer name: " + customer_name)
  print("Today's date: " + todays_date)
  print()
  print_menu(cart)