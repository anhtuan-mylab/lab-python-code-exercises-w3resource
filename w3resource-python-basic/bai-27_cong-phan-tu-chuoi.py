#Nội dung : Viết chương trình Python in ra màn hình một chuỗi bao gồm cộng các thành phần trong một List.
#

list = [1,5,12,2]
chuoi_moi = ""

for i in range(0, len(list)):
    chuoi_moi = chuoi_moi + str(list[i])

print("List : ", list)    
print("Chuỗi sau khi ghép : ", chuoi_moi)
 