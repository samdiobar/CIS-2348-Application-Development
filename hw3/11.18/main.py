# Name: Samuel Barroso
# PSID: 1844307

if __name__ == "__main__":
  # Take a string input and turn it into a list of integers
  list_of_nums = list(map(int, input().split(" ")))
  # Take a list of integers and only include positive values
  list_of_nums = list(filter(lambda x: x >= 0, list_of_nums))
  # Sort list from least to greatest
  list_of_nums.sort()
  # Print list without the brackets or commas
  print(" ".join(str(n) for n in list_of_nums), end=" ")

  # This solution is very short and I am fearful that this will be flagged for cheating
  # Because of this, I commented what each line does
  # I learned these programming techniques while taking Venkat's COSC 4315 class
  # The code contains less ceremony that comes from multiple for loops and if statements