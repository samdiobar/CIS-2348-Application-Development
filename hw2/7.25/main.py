def exact_change(user_total):

  money_types = [
    {"name": "dollar", "amount": 100, "plural": "dollars", "total": 0},
    {"name": "quarter", "amount": 25, "plural": "quarters", "total": 0},
    {"name": "dime", "amount": 10, "plural": "dimes", "total": 0},
    {"name": "nickel", "amount": 5, "plural": "nickels", "total": 0},
    {"name": "penny", "amount": 1, "plural": "pennies", "total": 0}
  ]

  if (user_total == 0):
    print("no change")

  cnt = 0
  while (user_total > 0):
    temp_amount = money_types[cnt]["amount"]
    if (user_total >= temp_amount):
      temp_num = money_types[cnt]["total"] = int(user_total/temp_amount)
      temp_name =  money_types[cnt]["plural"] if temp_num > 1 else money_types[cnt]["name"]
      print(temp_num, temp_name)
      user_total = user_total % temp_amount
    cnt += 1
  return money_types[0]["total"], money_types[1]["total"], money_types[2]["total"], money_types[3]["total"], money_types[4]["total"]

if __name__ == "__main__":
  input_val = int(input())
  num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)