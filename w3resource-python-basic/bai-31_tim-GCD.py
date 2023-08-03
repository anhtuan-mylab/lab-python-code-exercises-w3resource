#Nội dung : tìm GCD của a và b
#
def tim_gcd(a, b):
    gcd = 1
    if a%b == 0:
        return b
    for k in range(int(b/2), 0, -1):
        if a%k==0 and b%k==0:
            gcd = k
            break
    return gcd


a = input("Nhập a : ")
b = input("Nhập b : ")

print("GCD của %d và %d = %d"%(int(a),int(b),tim_gcd(int(a),int(b))))

