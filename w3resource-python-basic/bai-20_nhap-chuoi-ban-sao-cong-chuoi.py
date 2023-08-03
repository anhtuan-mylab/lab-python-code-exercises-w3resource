#Nội dung : Viết chương trình Python nhập vào một chuỗi bất kì và số bản sao (số bản sao phải dương). In ra màn hình chuỗi mới là ghép từ chuỗi  ban đầu và số bản sao.
#

chuoi = input("Nhập chuỗi : ")

while True:
    n = input("Nhập n bản sao (không âm) : ")
    if (int(n)<0):
        print("Nhập lại")
    else:
        break

ket_qua = ""

for i in range(0,int(n)):
    ket_qua = ket_qua + chuoi

print("\nChuỗi mới : " + ket_qua)