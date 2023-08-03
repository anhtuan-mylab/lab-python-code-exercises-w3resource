# Nội dung : In ra màn hình lịch (dạng theo tháng) từ tháng và năm nhập từ bàn phím.
#
import calendar

thang = input("Nhập tháng (month) : ")
nam = input("Nhập vào năm (year) : ")

print("\nIn ra màn hình lịch (theo tháng) : \n")
print(calendar.month(int(nam),int(thang)))
