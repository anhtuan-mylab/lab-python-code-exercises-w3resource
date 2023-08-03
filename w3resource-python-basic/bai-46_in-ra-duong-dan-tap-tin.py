#Nội dung : Viết chương trình Python in ra màn hình đường dẫn cảu tập tin đang thực thi.
#
import os

print("Đường dẫn tập tin : ", os.path.realpath(__file__))