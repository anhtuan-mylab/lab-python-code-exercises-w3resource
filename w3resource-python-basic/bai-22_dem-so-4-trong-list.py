# Nội dung : Viết chương trình Python cho trước một List gồm các số nguyên và đếm số lần 4 xuất hiện.
#
n = 0
list = [1,2,3,4,5,6,4]
#print(list)
for i in range(0,len(list)):
    if (list[i]==4):
        n = n + 1

print("List : ", list)
print("Số 4 xuất hiện : %d (lần)"%(n))
        