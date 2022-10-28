print("面包店正在打折，活动进行中")
strWeek=input("请输入中文星期（如星期一）：")
inttime=int(input("请输入时间中的小时（范围：0~23）："))
if(strWeek=="星期二" and (inttime>=19 and inttime<=20)) or (strWeek=="星期六" and (inttime>=17 and inttime<=18)):
     print("恭喜你")
else:
     print("很抱歉")
