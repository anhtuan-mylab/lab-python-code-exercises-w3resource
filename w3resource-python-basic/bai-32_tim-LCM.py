#Nội dung : tìm LCM từ a và b nhập từ bàn phím.
#

def tim_lcm(a,b):
    if a>b:
        z = a
    else:
        z = b
    while(True):
        if((z%a==0) and (z%b==0)):
            lcm = z
            break
        z+=1
    return lcm
    

a = input("Nhập a : ")
b = input("Nhập b : ")

print("LCM(%d, %d) : %d"%(int(a),int(b),tim_lcm(int(a),int(b))))
