# Name: Samuel Barroso
# PSID: 1844307

import datetime

def dateParse(input_file, output_file):
  # open input and create output files
  dates_file = open(input_file, 'r')
  output_file = open(output_file,'w')

  # array of months used later to determine if month in the date is valid
  # all month values are capitalized because they must be capitalized to be valid
  months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

  # reads first line in the input file
  line = dates_file.readline().replace("\n", "")
  # while loop iterates by reading each line until reaching the "-1" at the end of the file
  while (line != "-1"):
    # split the line of text into an array
    # split_line[0] should contain the month
    # split_line[1] should contain the day followed by a comma
    # split_line[2] should contain the year
    split_line = line.split(" ")
    # if split_line is not length = 3, then it is not a valid date since it does not have 3 values seperated by commas
    if (len(split_line) == 3):
      # checks to see if split_line[0] is a valid month
      if (split_line[0] in months):
        # checks to see if a comma is present
        if (split_line[1].find(",") > -1):
          # get todays date
          date_now = datetime.datetime.now()
          # checks if input date is before todays date
          if (int(split_line[2]) < int(date_now.strftime("%Y")) or (int(split_line[2]) == int(date_now.strftime("%Y")) and int(months.index(split_line[0])+1) < int(date_now.strftime("%m"))) or (int(split_line[2]) == int(date_now.strftime("%Y")) and int(months.index(split_line[0])+1) == int(date_now.strftime("%m")) and int(split_line[1].split(",")[0]) < int(date_now.strftime("%d")))):
            # write line to output file
            output_file.write(str(months.index(split_line[0])+1) + "/" + split_line[1].split(",")[0] + "/" + split_line[2] + "\n")
    # iterate to next line in input file
    line = dates_file.readline().replace("\n", "")
  # closes file reader and writer
  dates_file.close()
  output_file.close()

# main function
if __name__ == "__main__":

  # get input file name from user
  print("Please type input file name (Ex: \"input.txt\"): ",end="")
  input_file = str(input())

  # read through input file and writes valid dates to an output file named "parsedDates.txt"
  dateParse(input_file, "parsedDates.txt")