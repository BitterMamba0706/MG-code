print("有一个数，除三余二，除五余三，除七余二\n")
none=True
number=0
while none:
    number+=1
    if number%3==2 and number%5==3 and number%7==2:
        print("这个数是",number)
        none=False
    
