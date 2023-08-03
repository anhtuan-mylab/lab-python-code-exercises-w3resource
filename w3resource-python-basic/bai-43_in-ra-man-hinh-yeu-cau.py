#Nội dung : Viết chương trình Python in ra màn hình các yêu cầu như : os name, platform, platform release.
#
import os
import platform

print("Tên hệ điều hành : ", os.name)
print("Tên của loại hệ điều hành : ", platform.system())
print("Phiên bản của hệ điều hành : ", platform.release())