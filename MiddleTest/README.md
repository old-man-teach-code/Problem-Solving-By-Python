Mô tả:
Công ty ABC có một danh sách nhân viên và muốn sắp xếp danh sách này theo mức lương tăng dần để thuận tiện cho việc quản lý và tính toán chi phí. Mỗi nhân viên có các thông tin sau: Họ tên, Mã nhân viên, Chức vụ và Mức lương.

Yêu cầu:
1. Thiết kế một cấu trúc dữ liệu phù hợp để lưu trữ thông tin của mỗi nhân viên.

2. Viết một chương trình Python để đọc danh sách nhân viên từ một tệp văn bản có định dạng sau:
   ```
   Họ tên,Mã nhân viên,Chức vụ,Mức lương
   ```   
   Ví dụ:
   ```
   Nguyễn Văn A,NV001,Trưởng phòng,15000000
   Trần Thị B,NV002,Nhân viên,8000000
   ...
   ```
3. Sử dụng thuật toán sắp xếp để sắp xếp danh sách nhân viên theo mức lương tăng dần.

4. In ra danh sách nhân viên đã được sắp xếp theo định dạng:
   Họ tên - Mã nhân viên - Chức vụ - Mức lương

5. Tính tổng chi phí lương của công ty và in ra màn hình.

Lưu ý:
- Sinh viên cần sử dụng kiến thức về đọc/ghi tệp, cấu trúc dữ liệu, thuật toán sắp xếp và các kiến thức lập trình cơ bản đã học. 
- Nghiêm cấm sử dụng AI với mọi trường hợp, hình thức.
- Có thể sử dụng các công cụ tìm kiếm không tích hợp AI để tìm kiếm syntax nhưng không thể sử dụng để tìm kiếm thuật toán bất kỳ. (Nhấn mạnh là chỉ dùng để search syntax)
- Sinh viên cần đảm bảo mã nguồn rõ ràng, có chú thíchc comment đầy đủ và clean code.
- Để có file nhan_vien.txt, sinh viên cần chạy file nhan_vien_generate.py
- Để kiểm tra lại chạy check_data.py

Dữ liệu mẫu:
Tệp "nhan_vien.txt":
```
Nguyễn Văn A,NV001,Trưởng phòng,15000000
Trần Thị B,NV002,Nhân viên,8000000
Lê Hoàng C,NV003,Phó phòng,12000000
Phạm Văn D,NV004,Nhân viên,7500000
Hoàng Thị E,NV005,Nhân viên,9000000
```

Kết quả mong đợi:
```
Phạm Văn D - NV004 - Nhân viên - 7500000
Trần Thị B - NV002 - Nhân viên - 8000000
Hoàng Thị E - NV005 - Nhân viên - 9000000
Lê Hoàng C - NV003 - Phó phòng - 12000000
Nguyễn Văn A - NV001 - Trưởng phòng - 15000000

Tổng chi phí lương: 51500000
```