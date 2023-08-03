# Nội dung : Tính diện tích hình tròn dựa bán kính nhập từ bàn phím
# Công thức : S = r*r*3.14

import math
r = input("Nhap R tu ban phim : ")
s = float(r) * float(r) * math.pi
print("Dien tich hinh tron S = ", s)

# Trường hợp lấy 2 số thập phân
lay_2_so_tp = "{:.2f}".format(s)
print("Dien tich hinh tron S = ", lay_2_so_tp)