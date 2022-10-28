i=0
real=int(input("请输入商品的真实价格"))
while i<5:
    i=i+1
    guess=int(input("请输入你猜测的商品价格"))
    if real<guess:
        print("高了")
    elif real>guess:
        print("低了")
    else:
        print("恭喜你")
        break
if i>=5:
    print("很抱歉")


