def doc_du_lieu(ten_tap_tin):
    # Tạo 1 mảng để lưu danh sách nhân viên
    danh_sach_nhan_vien = []
    try:
        # Mở tập tin với quyền 'r' - tương đương với READ và lần lượt đọc
        with open(ten_tap_tin, 'r', encoding='utf-8') as file:
            # Lần lượt đọc từng dòng và ghi vào  mảng
            for line in file:
                ho_ten, ma_nv, chuc_vu, muc_luong = line.strip().split(',')
                nhan_vien = [ho_ten, ma_nv, chuc_vu, int(muc_luong)]
                # ghi vào mảng
                danh_sach_nhan_vien.append(nhan_vien)
    except FileNotFoundError:
        print(f"Không tìm thấy tệp '{ten_tap_tin}'")
    return danh_sach_nhan_vien

# Đọc dữ liệu từ tệp
ten_tap_tin = 'nhan_vien.txt'
# Gán dữ liệu mảng vào biến danh_sach_nhan_vien
danh_sach_nhan_vien = doc_du_lieu(ten_tap_tin)
print(f"Thành công tạo {len(danh_sach_nhan_vien)} bản ghi nhân viên")
if len(danh_sach_nhan_vien) > 0:
    print("Sample: ")
    print(f"{danh_sach_nhan_vien[0][0]} - {danh_sach_nhan_vien[0][1]} - {danh_sach_nhan_vien[0][2]} - {danh_sach_nhan_vien[0][3]}")
else:
    print("Không tồn tại hoặc tạo thất bại")