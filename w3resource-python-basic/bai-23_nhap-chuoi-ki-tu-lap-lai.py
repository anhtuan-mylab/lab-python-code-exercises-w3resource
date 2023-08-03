#Nội dung : Viết chương trình Python nhập vào một chuỗi và số kí tự được lấy. In ra màn hình chuỗi kí tự được lấy lặp lại. Trường hợp mà chuỗi chỉ có 1 kí tự thì lặp lại kí tự đó tùy theo số lần nhập.
#

chuoi = input("Nhập chuỗi : ")
n = input("Nhập số kí tự : ")

chuoi_moi = ""

for i in range(0, int(n)):
    chuoi_moi = chuoi_moi + chuoi[:int(n)]
    
print("Chuỗi mới : ",chuoi_moi)