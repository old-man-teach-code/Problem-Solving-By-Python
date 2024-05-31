import random

ho = ['Nguyễn', 'Trần', 'Lê', 'Phạm', 'Hoàng', 'Huỳnh', 'Phan', 'Vũ', 'Võ', 'Đặng']
ten_dem = ['Văn', 'Thị', 'Hoàng', 'Tuấn', 'Minh', 'Hồng', 'Quốc', 'Mỹ', 'Gia', 'Thành']
ten = ['An', 'Bình', 'Cường', 'Dung', 'Em', 'Giang', 'Hà', 'Khánh', 'Linh', 'Minh']

chuc_vu = ['Trưởng phòng', 'Phó phòng', 'Nhân viên']

# Mở 1 tập tin 'nhan_vien.txt' với quyền 'w' - tương đương với Write và lần lượt ghi
with open('nhan_vien.txt', 'w', encoding='utf-8') as file:
    # Lần lượt tạo dữ liệu cho từng dòng
    for i in range(1, 1001):
        ma_nv = f"NV{i:03d}"
        ho_ten = f"{random.choice(ho)} {random.choice(ten_dem)} {random.choice(ten)}"
        chuc_vu_nv = random.choice(chuc_vu)
        
        if chuc_vu_nv == 'Trưởng phòng':
            muc_luong = random.randint(15000000, 30000000)
        elif chuc_vu_nv == 'Phó phòng':
            muc_luong = random.randint(10000000, 20000000)
        else:
            muc_luong = random.randint(5000000, 15000000)
        # Ghi từng dòng
        file.write(f"{ho_ten},{ma_nv},{chuc_vu_nv},{muc_luong}\n")