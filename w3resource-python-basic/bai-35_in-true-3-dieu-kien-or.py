#Nội dung : trả về True khi a giống b, a+b=5 và | a-b | = 5
#
def tra_true(a, b):
    if ((a==b) or (a+b==5) or (abs(a-b)==5)):
        return True

a = input("Nhập a : ")
b = input("Nhập b : ")

print("Kết quả : ", tra_true(int(a), int(b)))

