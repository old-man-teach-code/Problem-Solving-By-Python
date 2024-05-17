def binary_search(arr, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return binary_search(arr, x, mid + 1, high)
    else:
        return binary_search(arr, x, low, mid - 1)

# Testing the function
arr = [1, 2, 3, 4, 5]
x = 3
print(binary_search(arr, x, 0, len(arr) - 1))  # 2
