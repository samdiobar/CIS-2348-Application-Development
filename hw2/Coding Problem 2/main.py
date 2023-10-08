

if __name__ == "__main__":
  dates_file = open('inputDates.txt', 'r')

  months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

  line = dates_file.readline()
  while (line != "-1"):
      split_line = line.split(" ")
      if (len(split_line) == 3):
        if (split_line[0] in months):
          print("good")
      print(len(split_line))

      line = dates_file.readline()