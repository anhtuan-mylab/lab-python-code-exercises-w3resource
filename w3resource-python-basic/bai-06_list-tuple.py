# Nhập dãy số ngăn cách bởi dấu phẩy và in thành List và Tuple 
# 

value = input("Nhập dãy số (ngăn cách bởi dấu phẩy) : ")
list = value.split(",")
print("List : ", list)

# Chuyển List thành Tuple 
tuple = tuple(list)
print("Tuple : ", tuple)
