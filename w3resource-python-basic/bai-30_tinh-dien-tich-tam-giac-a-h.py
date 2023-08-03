#Nội dung : Viết chương trình Python in ra màn hình kết quả tính diện tích của một tam giác cho biết độ dài chiều cao và cạnh đối diện từ đỉnh.
#

chieu_cao = input("Nhập chiều cao (height) : ")
canh_tu_dinh = input("Nhập cạnh từ định (base) : ")

dien_tich = (float(chieu_cao)*float(canh_tu_dinh))/2

print("Diện Tích tam giác : ", float(dien_tich))
