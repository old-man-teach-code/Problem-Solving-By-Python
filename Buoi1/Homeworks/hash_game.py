import time
import os

# Mảng chứa tất cả các chữ cái không viết hoa
lowercase_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]

# Mảng chứa tất cả các chữ cái viết hoa
uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

# Hàm check_password(input_password: str) -> bool nhận vào một chuỗi input_password và trả về True nếu chuỗi đúng mật khẩu
def check_password(input_password: str) -> bool:
    hashed_password = simple_hash_function(input_password)
    if hashed_password == "32aff7":
        return True
    return False


def simple_hash_function(input_string: str) -> str:
    hash_value = 0
    for char in input_string:
        ascii_value = ord(char)
        hash_value = (hash_value * 31 + ascii_value) % (10**9 + 7)
    hashed_string = hex(hash_value)[2:]
    return hashed_string

def find_password():
    characters = lowercase_letters
    n = 0
    for a1 in characters:
        for a2 in characters:
            for a3 in characters:
                for a4 in characters:
                    n = n + 1
                    password = a1 + a2 + a3 + a4
                    print(f"Lần thử thứ {n} {password}")
                    os.system("clear")
                    check_password(password)
                    if check_password(password):
                        print("Mật khẩu đúng")
                        return password
    print("Sai mật khẩu")
    return ""
            
        
    
    check_password(password)
    if check_password(password):
        print("Mật khẩu đúng")
        return password
    else:
        print("Sai mật khẩu")
        return ""

def main():
    # process time calculation 
    start = time.time()
    print("----------------------------")
    password = find_password()
    print(f"Mật khẩu cần tìm là: {password}")
    end = time.time()
    print(f"Thời gian chạy: {end - start} giây")
    print("----------------------------")


if __name__ == '__main__':
    main()



