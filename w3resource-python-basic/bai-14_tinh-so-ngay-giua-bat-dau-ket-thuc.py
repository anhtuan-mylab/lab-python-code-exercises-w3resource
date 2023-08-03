# Nội dung : Tính số ngày giữa ngày bắt đầu và ngày kết thúc.
#

from datetime import date
from datetime import datetime

# Nhập vào thời gian bắt đầu 
nhap_bat_dau = input("Nhập vào thời gian bắt đầu : ")
list_bd = nhap_bat_dau.split(",")
for i in range(0, len(list_bd)):
    list_bd[i] = int(list_bd[i])
    
tuple_bd = tuple(list_bd)
tg_bat_dau = date(*tuple_bd)

# nhập vào thời gian kết thúc
nhap_ket_thuc = input("Nhập vào thời gian kết thúc (theo dạng ngày,tháng,năm) : ")
list_kt = nhap_ket_thuc.split(",")
for i in range(0, len(list_kt)):
    list_kt[i] = int(list_kt[i])
    
tuple_kt = tuple(list_kt)
tg_ket_thuc = date(*tuple_kt)

# In ra kết quả
print("Thời gian bắt đầu : ", tg_bat_dau)
print("Thời gian kết thúc : ", tg_ket_thuc)

print("Số ngày : ", (tg_ket_thuc-tg_bat_dau).days)
