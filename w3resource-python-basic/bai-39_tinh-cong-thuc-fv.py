#Nội dung : Viết chương trình Python cho các giá trị và tính công thức : FV = P(1 + r/n)^nt.
#

amt = 10000
int = 3.5
years = 7

future_values = amt*((1+(0.01*int)) ** years)

print("Các giá trị : amt = 10000, int = 3.5, years = 7")
print("Kết quả tính FV : ", round(future_values, 2))