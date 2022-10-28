NBA=('lebron','curry','KD','kawi','GA','harden')
print(NBA[3])

NBA=('lebron','curry','KD','kawi','GA','harden')
print("hi,welcome\n")
for name in NBA:
    print(name+"player  ",end=" ")

NBA=('lebron','curry','KD','kawi','GA','harden')
print("\n")
for index,item in enumerate(NBA):
    if index%2==0:
        print(item+",",end='')
    else:
        print(item+".",end='')
