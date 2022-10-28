import random
num=(random.randint(10,100) for i in range(10))
print("原",num)
num=tuple(num)
print("现",num)

num=(i for i in range(3))
print(num.__next__())
print(num.__next__())
print(num.__next__())
num=tuple(num)
print("转",num)

num=(i for i in range(4))
for i in num:
    print(i,end="")
print(tuple(num))
