verse1=["0","1","2"]
del verse1[-1]
print(verse1)

verse2=["3","4","5"]
verse2.remove("5")
print(verse2)

verse3=["6","7","8"]
value="8"
if verse3.count(value)>0:
    verse3.remove(value)
print(verse3)
