#Nội dung : Viết chương trình Python tính tổng của 2 số nguyên nhập từ bàn phím. In ra màn hình tổng, nếu tổng nằm trong khoảng 15 → 20 thì in ra 20.
#

a = input("Nhập số a : ")
b = input("Nhập số b : ")

tong = int(a) + int(b)

if (tong > 15 and tong < 20):
    print("Tổng ban đầu là : ", tong)
    print("Tổng thay đổi : 20")
else:
    print("Do tổng không trong khoảng 15 - 20 nên tổng là : ", tong)