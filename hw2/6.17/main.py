# Name: Samuel Barroso
# PSID: 1844307

def passwordChecker(user_input):
  result = user_input

  result = result.replace("i", "!")
  result = result.replace("a", "@")
  result = result.replace("m", "M")
  result = result.replace("B", "8")
  result = result.replace("o", ".")
  result = result + "q*s"

  return result

if __name__ == "__main__":
  input_val = str(input())
  print(passwordChecker(input_val))