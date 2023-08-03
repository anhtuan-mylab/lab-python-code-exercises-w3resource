# Nội dung : In ra kết quả phép tính hiệu (a-17) với a nhập từ bàn phím. Nếu giá trị âm thì lấy giá trị tuyệt đối.
#
a = input("Nhập số a : ")
hieu = float(a)-17.0
if (hieu<0):
    print("Do %d bé hơn 17 nên hiệu (%d - 17) là : %d và giá trị tuyệt đối |12-17| : %d"%(float(a),float(a),hieu,abs(hieu)))
else:
    print("Do %d lớn hơn 17 nên hiệu (%d - 17) là : %d" % (float(a),float(a),hieu))
