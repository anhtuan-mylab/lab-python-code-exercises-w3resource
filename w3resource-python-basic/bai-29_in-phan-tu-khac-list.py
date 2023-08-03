#Nội dung : Viết chương trình Python cho hai list (color-list-01 và color-list-02). Kết quả in ra màn hình màu sắc không có trong color-list-02
#

color_list_01 = ["White", "Black", "Red"]
color_list_02 = ["Red", "Green"]

list_ket_qua = []

for i in range(0, len(color_list_01)):
    for x in range(0, len(color_list_02)):
        if (color_list_01[i]!=color_list_02[x]):
            list_ket_qua.append(color_list_01[i])
            break
        if (color_list_01[i]==color_list_02[x]):
            break

print("Color List 01 : ", color_list_01)
print("Color List 02 : ", color_list_02)
print("Kết quả : ", list_ket_qua)