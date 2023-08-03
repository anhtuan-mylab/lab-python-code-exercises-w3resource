# Nội dung : tính tổng 3 số nguyên nhập từ bàn phím, nếu số giống nhau thì tổng bằng 0.
#

a = input("Nhập a : ")
b = input("Nhập b : ")
c = input("Nhập c : ")

if ((a==b) or (a==c) or (b==c)):
    print("Tổng 3 số là : 0")
else:
    print("Tổng 3 số khác nhau : ", int(a)+int(b)+int(c))