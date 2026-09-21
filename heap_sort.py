def heapify(arr, n, i):
    largest = i          # Initialize largest as root
    left = 2 * i + 1     # Left child index
    right = 2 * i + 2    # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # 1. Build Max-Heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 2. Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move current root to end
        heapify(arr, i, 0)               # Call heapify on reduced heap

# Example execution:
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print(arr)  # Output: [5, 6, 7, 11, 12, 13]
