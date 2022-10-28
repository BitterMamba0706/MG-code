import random
num=[random.randint(10,100) for i in range(10)]
print("随机数是",num)

num2=[423,32,43,42,4,234,32,423,342]
num3=[int(x*0.5) for x in num2]
print(num2)
print(num3)

num4=[3284,3,23,4,64,77,89,6,8,56,32,43,24]
num5=[x for x in num4 if x>10]
print("原",num4)
print("现",num5)
