#Nội dung : Viết một chương trình Python dựa vào một List chứa số và một biểu tượng. Tạo nên một Histogram dựa trên những số trong List. 
#
bieu_tuong = "@"
list = [2,3,6,5]

print("List : ", list)
print("Biểu tượng : ", bieu_tuong)

print("\nHistogram : ")
for i in range(0, len(list)):
    for a in range(0, list[i]):
        print(bieu_tuong, end = " ")
    print("\t")