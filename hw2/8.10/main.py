# Name: Samuel Barroso
# PSID: 1844307

def palindrome(user_input):
  text = user_input.replace(" ", "")

  for i in range(0,int(len(text))):
    if (text[i] != text[int(len(text)) - i - 1]):
      return user_input + " is not a palindrome"
  return user_input + " is a palindrome"

if __name__ == "__main__":
  user_input = str(input())
  print(palindrome(user_input))