#Nội dung : Viết chương trình Python nhập vào một kí tự và kiểm tra xem kí tự đó có phải là nguyên âm (nguyên âm : u,e,o,a,i)
#
while True:
    ki_tu = input("Nhập vào 1 kí tự : ")
    if (len(ki_tu)>1):
        print("Chỉ được nhập 1 kí tự.")
    else:
        break
        

list_nguyen_am = ['u','e','o','a','i']

if ki_tu in list_nguyen_am:
    print("Kí tự %s là nguyên âm."%(ki_tu))
else:
    print("Kí tự %s không phải là nguyên âm."%(ki_tu))
    


