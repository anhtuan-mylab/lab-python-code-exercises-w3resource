#Nội dung : Viết chương trình Python in ra số Thread trên CPU đang sử dụng.
#

import multiprocessing
import os

print("Sử dụng multiprocessing : ", multiprocessing.cpu_count())
print("Sử dụng os : ", os.cpu_count())
