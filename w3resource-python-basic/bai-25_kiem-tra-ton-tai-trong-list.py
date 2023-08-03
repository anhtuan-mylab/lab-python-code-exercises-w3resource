#Nội dung : Viết chương trình Python cho trước một List chứa các số và nhập vào một số bất kì. Kiểm tra kết quả trả về giá trị True hay False.
#
n = input("Nhập vào 1 số bất kì : ")
list_so = [1,5,8,3]

print("List : ", list_so)

if int(n) in list_so:
    print("True")
else:
    print("False")

