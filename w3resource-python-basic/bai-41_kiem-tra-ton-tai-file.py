#Nội dung : kiểm tra sự tồn tại của một tập tin.
#
import os.path

path_01 = "bai-01.py"
path_02 = "bai-01-test.py"

print("Kết quả : ", os.path.isfile(path_01))
print("Kết quả : ", os.path.isfile(path_02))