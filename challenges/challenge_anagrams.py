def partition(arr, low_index, high_index):
    # Select the pivot element as the first index element
    partition_index = arr[low_index]
    # start the left pointer
    i = low_index + 1
    # right pointer
    j = high_index

    while True:
        # move the left pointer until finding an element greater than the pivot
        while i <= j and arr[i] <= partition_index:
            i += 1
        # the same for the right pointer
        while i <= j and arr[j] >= partition_index:
            j -= 1
        if i > j:
            break
        # Swap the elements at the left and right
        arr[i], arr[j] = arr[j], arr[i]

    # Swap the element at the right pointer with the pivot
    arr[low_index], arr[j] = arr[j], arr[low_index]
    return j


def quicksort(arr, low_index, high_index):
    if low_index < high_index:
        # Partition the array and get the pivot index
        partition_index = partition(arr, low_index, high_index)
        # Recursivity the arrays before and after the partition
        quicksort(arr, low_index, partition_index - 1)
        quicksort(arr, partition_index + 1, high_index)


def sort_string(string):
    # Convert to a list of characters
    chars = list(string)
    quicksort(chars, 0, len(chars) - 1)
    # Convert the sorted elements back to a string with join
    return "".join(chars)


def is_anagram(first_string, second_string):
    firstString = first_string.lower()
    secondString = second_string.lower()
    # check if strings are empty
    if firstString == "" and secondString == "":
        return (firstString, secondString, False)
    # Sort the strings
    sorted_first = sort_string(firstString)
    sorted_second = sort_string(secondString)
    return sorted_first, sorted_second, sorted_first == sorted_second
