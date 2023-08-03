# Nội dung : Viết chương trình Python trả về giá trị True hoặc false của phép tính abs(1000-n) hoặc abs(2000-n) ≤ 100
#
def xet_gia_tri(n):
    return ((abs(1000-n)<=100) or (abs(2000-n)<=100))
   
i = input("Nhập số i : ")
print("Với %d thì : %s" % (float(i),xet_gia_tri(float(i))))