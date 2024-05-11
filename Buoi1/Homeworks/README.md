# Bài Tập Python - Brute Force

- Đây là bài tập về phương pháp Brute Force trong Python. Mục tiêu của bài tập này là giúp bạn làm quen với cách giải quyết các bài toán thông qua phương pháp brute force, tức là duyệt qua tất cả các trường hợp có thể để tìm ra kết quả.
- Sau khi đạt được mục tiêu, bạn sẽ có thể tối ưu hóa các giải pháp của mình thông qua các phương pháp khác như sử dụng các cấu trúc dữ liệu phù hợp, sử dụng các thuật toán tối ưu hơn, ...
- Mục tiêu là giải quyết được vấn đề, không phải là giải quyết nhanh nhất. Bạn có thể sử dụng bất kỳ cách giải quyết nào mà bạn biết, miễn là nó hoạt động đúng.



## Mục Lục

1. [Tìm số lớn nhất và số nhỏ nhất trong mảng](#1-tìm-số-lớn-nhất-và-số-nhỏ-nhất-trong-mảng)
2. [Kiểm tra số chính phương](#2-kiểm-tra-số-chính-phương)
3. [Tìm ước số](#3-tìm-ước-số)
4. [Giải mã mật khẩu đơn giản](#4-giải-mã-mật-khẩu-đơn-giản)
5. [Tính số Fibonacci thứ n](#5-tính-số-fibonacci-thứ-n)
6. [Đảo ngược chuỗi](#6-đảo-ngược-chuỗi)
7. [Kiểm tra số đối xứng](#7-kiểm-tra-số-đối-xứng)
8. [Đếm số lẻ trong mảng](#8-đếm-số-lẻ-trong-mảng)
9. [Tìm phần tử xuất hiện nhiều nhất](#9-tìm-phần-tử-xuất-hiện-nhiều-nhất)
10. [Tìm cặp số có tổng bằng target](#10-cho-một-mảng-số-nguyên-arr-và-một-số-nguyên-target-tìm-tất-cả-các-cặp-số-trong-mảng-có-tổng-bằng-target)

## 1. Tìm số lớn nhất và số nhỏ nhất trong mảng

**Đầu vào**: Một danh sách các số nguyên.

**Đầu ra**: Hai số nguyên, số lớn nhất và số nhỏ nhất trong danh sách.

**Ví dụ**:

- Đầu vào: `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]`
- Đầu ra: `9, 1`

- Đầu vào: `[-1, -3, -5, -7]`
- Đầu ra: `-1, -7`

## 2. Kiểm tra số chính phương

**Đầu vào**: Một số nguyên `n`.

**Đầu ra**: `True` nếu `n` là số chính phương, ngược lại `False`.

**Ví dụ**:

- Đầu vào: `16`
- Đầu ra: `True`

- Đầu vào: `20`
- Đầu ra: `False`

## 3. Tìm ước số

**Đầu vào**: Một số nguyên `n`.

**Đầu ra**: Danh sách các ước số của `n`.

**Ví dụ**:

- Đầu vào: `28`
- Đầu ra: `[1, 2, 4, 7, 14, 28]`

- Đầu vào: `13`
- Đầu ra: `[1, 13]`

**Gợi ý**: Duyệt qua các số từ 1 đến `n` và kiểm tra xem chúng có phải là ước số của `n` hay không.

## 4. Giải mã mật khẩu đơn giản

**Đầu vào**: Một chuỗi bí mật và chuỗi mật khẩu.

**Đầu ra**: `True` nếu chuỗi mật khẩu là hoán vị của chuỗi bí mật, ngược lại `False`.

**Ví dụ**:

- Đầu vào: Bí mật `"abc"`, Mật khẩu `"bca"`
- Đầu ra: `True`

- Đầu vào: Bí mật `"abc"`, Mật khẩu `"abd"`
- Đầu ra: `False`

**Gợi ý**: Sử dụng phương pháp brute force để sinh tất cả các hoán vị của chuỗi mật khẩu và so sánh chúng với chuỗi bí mật.

## 5. Tính số Fibonacci thứ n

**Đầu vào**: Một số nguyên `n`.

**Đầu ra**: Số Fibonacci thứ `n`.

**Ví dụ**:

- Đầu vào: `7`
- Đầu ra: `13`

- Đầu vào: `10`
- Đầu ra: `55`

**Gợi ý**: Dãy số Fibonacci là dãy số bắt đầu từ 0 và 1, các số tiếp theo được tính bằng cách cộng hai số trước đó. Ví dụ: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... 

## 6. Đảo ngược chuỗi

**Đầu vào**: Một chuỗi ký tự.

**Đầu ra**: Chuỗi đảo ngược.

**Ví dụ**:

- Đầu vào: `"hello"`
- Đầu ra: `"olleh"`

- Đầu vào: `"world"`
- Đầu ra: `"dlrow"`

**Gợi ý**: Duyệt qua chuỗi từ cuối về đầu và thêm các ký tự vào chuỗi kết quả.

## 7. Kiểm tra số đối xứng

**Đầu vào**: Một số nguyên `n`.

**Đầu ra**: `True` nếu `n` là số đối xứng, ngược lại `False`.

**Ví dụ**:

- Đầu vào: `121`
- Đầu ra: `True`

- Đầu vào: `123`
- Đầu ra: `False`

**Gợi ý**: Dùng phép chia và lấy dư để tách số `n` thành các chữ số rồi so sánh chúng để kiểm tra xem `n` có đối xứng hay không.

## 8. Đếm số lẻ trong mảng

**Đầu vào**: Một mảng các số nguyên.

**Đầu ra**: Số lượng các số lẻ trong mảng.

**Ví dụ**:

- Đầu vào: `1, 2, 3, 4, 5`
- Đầu ra: `3`

- Đầu vào: `2, 4, 6, 8`
- Đầu ra: `0`

**Gợi ý**: Duyệt qua mảng và tăng biến đếm mỗi khi gặp một số lẻ.

## 9. Tìm phần tử xuất hiện nhiều nhất

**Đầu vào**: Một mảng các phần tử.

**Đầu ra**: Phần tử xuất hiện nhiều nhất trong mảng.

**Ví dụ**:

- Đầu vào: `1, 3, 3, 3, 2, 4, 4, 4, 5`
- Đầu ra: `3` hoặc `4` (giả sử có hai phần tử xuất hiện cùng số lần nhiều nhất)

- Đầu vào: `1, 1, 2, 2, 3, 3`
- Đầu ra: `1`, `2`, hoặc `3` (nếu tất cả đều xuất hiện với tần suất như nhau)

- Đầu vào: `1, 2, 3, 4, 5, 5`
- Đầu ra: `5`

**Gợi ý**: Sử dụng một bộ đếm (counter) để đếm số lần xuất hiện của mỗi phần tử trong mảng. Sau đó, tìm phần tử có số lần xuất hiện nhiều nhất. Bộ đếm có thể được tạo bằng cách duyệt qua mảng và tăng giá trị tương ứng với mỗi phần tử.

## 10. Cho một mảng số nguyên arr và một số nguyên target, tìm tất cả các cặp số trong mảng có tổng bằng target.

**Đầu vào**: Một mảng các số nguyên arr và một số nguyên target.

**Đầu ra**: Danh sách các cặp số (phần tử trong mảng) có tổng bằng target. Mỗi cặp số được biểu diễn dưới dạng một mảng con gồm hai phần tử.

**Ví dụ**:

- Đầu vào: arr = [1, 2, 3, 4, 5], target = 5
- Đầu ra: [[1, 4], [2, 3]]

- Đầu vào: arr = [1, 1, 2, 3], target = 4
- Đầu ra: [[1, 3], [1, 3]] (Cặp số 1 và 3 xuất hiện hai lần vì có hai phần tử 1 trong mảng)

- Đầu vào: arr = [1, 2, 3, 4, 5], target = 10
- Đầu ra: [] (Không có cặp số nào có tổng bằng 10)

**Gợi ý**: Sử dụng phương pháp brute force để duyệt qua tất cả các cặp số có thể có trong mảng. Để tránh cặp số trùng lặp, bạn có thể sử dụng một cấu trúc dữ liệu set để lưu trữ các cặp số đã duyệt qua.
