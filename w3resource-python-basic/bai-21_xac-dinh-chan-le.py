# Nội dung : Viết chương trình Python nhập một số bất kì từ bàn phím (số nguyên) và kiểm tra xem số đó là chẵn hay lẽ. In ra màn hình kết quả tìm được.
#
n = input("Nhập số nguyên n : ")

if (int(n)%2==0):
    print("Số %d là số chẵn."%(int(n)))
else:
    print("Số %d là số lẻ."%(int(n)))