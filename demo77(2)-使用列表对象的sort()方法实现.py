num=[31,31241,4,14,124,12,412413,4,14,21,4,14,214]
print("原",num)
num.sort()
print("升",num)
num.sort(reverse=True)
print("降",num)

char=["fh","Aa","da","Vv","ga","ww"]
char.sort()#默认区分大小写
print("区分大小写的排序是",char)
char.sort(key=str.lower)
print("不区分大小写的排序是",char)
