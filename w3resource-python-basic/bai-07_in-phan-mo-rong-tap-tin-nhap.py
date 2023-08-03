# Nhập chuỗi dạng <ten>.<duoi_file> và in ra màn hình đuôi file.

chuoi = input("Nhập tên file + phần mở rộng (vd: text.txt) : ")
list = chuoi.split(".")

print("Phần mở rộng : ", list[-1])