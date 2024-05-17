def count_elements(arr, low, high):
    if low > high:
        return 0
    elif low == high:
        return 1
    else:
        mid = (low + high) // 2
        left_count = count_elements(arr, low, mid)
        right_count = count_elements(arr, mid + 1, high)
        return left_count + right_count

# Testing the function
arr = [1, 2, 3, 4, 5]
print("Số lượng phần tử:", count_elements(arr, 0, len(arr) - 1))  # 5
