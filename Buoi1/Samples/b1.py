import random

# Khai báo mảng A rỗng (không có phần tử nào)
A = []
# Tạo 1 vòng lặp 100 lần lặp để thêm 100 phần tử ngẫu nhiên vào mảng A
for i in range(100):
    # Tạo 1 số ngẫu nhiên từ 0 đến 100
    ran_int = random.randint(0, 100)
    # Thêm số ngẫu nhiên vào mảng A
    A.append(ran_int)

# TODO: Nhập vào 1 số x bất kỳ từ bàn phím và kiểm tra số x đó có trong mảng A hay không? 
#TODO: Nếu có thì in ra "YES" và ngược lại in ra "NO"
print(A)

def find(x):
    for i in A:
        print(f"Kiểm tra số {i}")
        if(i == x):
            print("YES")
            return
    print("NO")

# Nhập vào 1 số x từ bàn phím
x = int(input("Nhập vào 1 số x = "))
find(x)

        