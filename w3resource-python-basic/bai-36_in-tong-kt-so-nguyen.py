#Nội dung : nhập a và b - phải là số nguyên (báo lỗi nếu không phải) + tính tổng.
#
try:
    a = int(input("Nhập a : "))
    b = int(input("Nhập b : "))
    
    print("Tổng là : ", a+b)
    
except ValueError:
    print("Hai số phải là số nguyên.")