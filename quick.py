def partition(arr, l, r):
    pivot = arr[l]  # Select leftmost element as pivot
    i = l - 1
    j = r + 1

    while True:
        # Move i right while arr[i] < pivot
        i += 1
        while arr[i] < pivot:
            i += 1

        # Move j left while arr[j] > pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If pointers cross, partition is complete
        if i >= j:
            return j

        # Swap elements at i and j inside the loop
        arr[i], arr[j] = arr[j], arr[i]


def quickSort(arr, l, pivot_index, r):
    if l < r:
        pivot_index = partition(arr, l, r)
        # Pass 4 arguments to match the function signature
        quickSort(arr, l, 0, pivot_index)  # Left subarray
        quickSort(arr, pivot_index + 1, 0, r)  # Right subarray


# Example execution:
arr = [10, 7, 8, 9, 1, 5]
quickSort(arr, 0, 0, len(arr) - 1)
