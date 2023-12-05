# Name: Samuel Barroso
# PSID: 1844307

if __name__ == "__main__":
    sentence1 = input().split(" ")
    sentence2 = input().split(" ")

    for i in range(0, len(sentence1)):
        if (sentence1[i] != sentence2[i]):
            print(f'{sentence1[i]} {sentence2[i]}')