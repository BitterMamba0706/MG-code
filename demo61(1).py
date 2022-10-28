total=0
for number in range(1,100,1):
    if number%2==1:
        continue
    total+=number
print("1到100（不包括100）的偶数和是",total) 
