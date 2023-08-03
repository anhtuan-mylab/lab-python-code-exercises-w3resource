# Nội dung : Viết chương trình Python nhập vào một chuỗi. Xét kí tự đầu tiên là Is trong chuỗi vừa nhập. Nếu đã có thì trả về nguyên mẫu (tức giữa nguyên) và nếu không có thì in ra màn hình chuỗi sau khi thêm Is vào đầu chuỗi.
#
chuoi = input("Nhập chuỗi : ")
if (len(chuoi)>=2 and chuoi[:2] == "Is"):
    print("Chuỗi giữ nguyên : " + chuoi)
else:
    print("Chuỗi phải thêm kí tự : " + "Is"+chuoi)