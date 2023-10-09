# Name: Samuel Barroso
# PSID: 1844307

import csv

def frequencies(input_file):
  word_dict = {}

  text = open(input_file, 'r').read().replace("\n", "").split(",")
  for word in text:
    if (word not in word_dict):
      word_dict[word] = 1
    else:
      word_dict[word] += 1
  for word in word_dict:
    print(word, word_dict[word])

if __name__ == "__main__":
  user_input = str(input())
  frequencies(user_input)