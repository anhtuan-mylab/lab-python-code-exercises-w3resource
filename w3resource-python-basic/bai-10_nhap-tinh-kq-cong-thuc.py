# Nhập số n (số nguyên) và tính kết quả công thức : n + nn + nnn

n = input("Nhập số n : ")
nn = n+n
nnn = n+n+n

cong_thuc = int(n) + int(nn) + int(nnn)

print("Kết quả : ", cong_thuc)