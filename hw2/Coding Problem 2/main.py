import datetime

def dateParse(input_file, output_file):
  dates_file = open(input_file, 'r')
  output_file = open(output_file,'w')

  months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

  line = dates_file.readline().replace("\n", "")
  while (line != "-1"):
    split_line = line.split(" ")
    if (len(split_line) == 3):
      if (split_line[0] in months):
        if (len(split_line[1].split(",")) == 2):
          date_now = datetime.datetime.now()
          if (int(split_line[2]) < int(date_now.strftime("%Y")) or (int(split_line[2]) == int(date_now.strftime("%Y")) and int(months.index(split_line[0])+1) < int(date_now.strftime("%m"))) or (int(split_line[2]) == int(date_now.strftime("%Y")) and int(months.index(split_line[0])+1) == int(date_now.strftime("%m")) and int(split_line[1].split(",")[0]) < int(date_now.strftime("%d")))):
            output_file.write(str(months.index(split_line[0])+1) + "/" + split_line[1].split(",")[0] + "/" + split_line[2] + "\n")
    line = dates_file.readline().replace("\n", "")
  dates_file.close()
  output_file.close()

if __name__ == "__main__":
  print("Please type input file name (Ex: \"input.txt\"): ",end="")
  input_file = str(input())
  dateParse(input_file, "parsedDates.txt")