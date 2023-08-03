#Nội dung : Viết chương trình Python kiểm tra xem hệ điều hành chạy trên 32-bit hay 64-bit.
#

import sys
import struct

print("Sử dụng sys.version : ")
print(sys.version)

print("\nSử dụng calcsize : %s (bit)"%(struct.calcsize('P')*8))