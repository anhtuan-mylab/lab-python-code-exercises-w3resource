from datetime import datetime 

# In ra theo thông thường -> Kết quả : 2023-07-25 12:50:27.647568 
print("Hien tai 01 : " + str(datetime.now()))

# Nếu muốn in theo dạng dd/mm/YY và  H:M:S
now = datetime.now()
print("Hien Tai 02 : " + now.strftime("%d/%m/%Y %H:%M:%S"))