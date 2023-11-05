# Name: Samuel Barroso
# PSID: 1844307

if __name__ == "__main__":
  # Convert string input into a list of strings
  input_list = input().split(" ")
  # Creates a dictionary from input_list with the following key:value pair
  # Key = String from input_list
  # Value = Frequency of key in input_list
  freq_dict = {input_list[i]: input_list.count(input_list[i]) for i in range(0, len(input_list))}
  # Print dictionary key value pairs with each string from input_list in original order
  print("\n".join((string + " " + str(freq_dict[string])) for string in input_list))

  # This solution is very short and I am fearful that this will be flagged for cheating
  # Because of this, I commented what each line does
  # I learned these programming techniques while taking Venkat's COSC 4315 class
  # The code contains less ceremony that comes from multiple for loops and if statements