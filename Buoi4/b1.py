# Cho 1 mảng A gỗm n phần tử (có sắp xếp), tìm phần tử x nhập vào từ bàn phím có trong mảng A hay không?
import random

arr = sorted(random.sample(range(0, 9999), 10))
print(arr)
def find(arr, min, max, x):
    try:
        if max >= min:
            mid = min + (max - min) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return find(arr, min, mid - 1, x)
            else:
                return find(arr, mid + 1, max, x)
        else:
            return -1
    except Exception:
        print(e)

x = int(input("Nhap vao so x can tim"))

index = find(arr, 0, len(arr) - 1, x)
if index == -1:
    print("Khong co")
else:
    print(f"So can tim o vi tri {index} gia tri = " + str(arr[index]))
