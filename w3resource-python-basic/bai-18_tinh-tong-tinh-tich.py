# Nội dung : Viết chương trình Python nhập vào 3 số bất kì và tính tổng (nếu 3 số khác nhau) hay tính tích (nếu 3 số giống nhau).
#
def tinh_cong(a,b,c):
    return (float(a)+float(b)+float(c))

def tinh_tich(a,b,c):
    return (float(a)*3)
    
a = input("Nhập số a : ")
b = input("Nhập số b : ")
c = input("Nhập số c : ")

if (a != b != c):
    print("Do a,b,c khác nhau nên tính cộng : %d" %(tinh_cong(a,b,c)))
if (a==b==c):
    print("do a,b,c giống nhau nên tính tích : %d" %(tinh_tich(a,b,c)))

