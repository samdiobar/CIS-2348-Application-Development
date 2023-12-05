# Name: Samuel Barroso
# PSID: 1844307

def selection_sort_descend_trace(list):
    for i in range(0,len(list)-1):
        sub_list = list[i:]
        largest = max(sub_list)
        list[sub_list.index(largest) + i], list[i] = list[i], list[sub_list.index(largest) + i]

        print(" ".join(str(item) for item in list) + " ")

if __name__ == "__main__":
    nums = [int(i) for i in input().split()]
    selection_sort_descend_trace(nums)