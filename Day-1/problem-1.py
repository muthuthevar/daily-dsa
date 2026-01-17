# Remove duplcates from sorted array 2 - leetcode - 80


def removeDuplicates(arr):
    i, j = 0, 0

    while j < len(arr):
        if i < 2 or arr[i - 2] != arr[j]:
            arr[i] = arr[j]
            i += 1
        j += 1
    print(arr)


removeDuplicates([1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5])
