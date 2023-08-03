#Nội dung : Viết chương trình Python nhập vào tọa độ 2 điểm A(x1, y1) và B(x2, y2). In ra màn hình tính khoảng cách giữa 2 điểm đó.
#
import math
try:
    toa_do_a = input("Nhập tọa độ a(x1, y1) : ")
    list_a = toa_do_a.split(",")

    toa_do_b = input("Nhập tọa độ b(x2, y2) : ")
    list_b = toa_do_b.split(",")

    khoang_cach = math.sqrt(((int(list_a[0]) - int(list_b[0]))**2) + ((int(list_a[1]) - int(list_b[1]))**2))
    
    print("Kết quả : ", khoang_cach)
except ValueError:
    print("Lỗi.")
