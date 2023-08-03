#Nội dung : Viết chương trình Python in ra màn hình không xuống dòng khi sử dụng for.
#
print("Sử dụng for mặc định : ")
for i in range(0,10):
    print("*")

print("\nSử dụng for mà không xuống dòng :")
for x in range(0, 10):
    print("*", end="")
    