arr = list(map(int, input("Nhập mảng: ").split(',')))
print(arr)

min = arr[0]
max = arr[0]

for i in arr:
    if i < min:
        min = i
    if i > max:
        max = i
print(f"Giá trị nhỏ nhất là: {min}, Giá trị lớn nhất là: {max}")