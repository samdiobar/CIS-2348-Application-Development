# Name: Samuel Barroso
# PSID: 1844307

# Global variable
num_calls = 0

# TODO: Write the partitioning algorithm - pick the middle element as the 
#       pivot, compare the values using two index variables l and h (low and high), 
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary
def partition(user_ids, i, k):
    pivot_pos = int(round((i+k)/2, 0))
    user_ids[i], user_ids[pivot_pos] = user_ids[pivot_pos], user_ids[i]
    pivot = user_ids[i]
    low = i+1
    high = k
    while (low <= high):
        while (user_ids[high] > pivot):
            high -= 1
        while (low <= high and user_ids[low] <= pivot):
            low = low + 1
        if (low <= high):
            user_ids[low], user_ids[high] = user_ids[high], user_ids[low]
            low += 1
            high -= 1
    user_ids[i], user_ids[high] = user_ids[high], user_ids[i]
    return high

# TODO: Write the quicksort algorithm that recursively sorts the low and 
#       high partitions. Add 1 to num_calls each time quisksort() is called
def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1
    if (i < k):
        index = partition(user_ids, i, k)
        quicksort(user_ids, i, index-1)
        quicksort(user_ids, index+1, k)

if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)