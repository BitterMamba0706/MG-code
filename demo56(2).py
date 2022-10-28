print("有一数，除三余二，除五余三，除七余二\n")
for number in range(100):
    if number%3==2 and number%5==3 and number%7==2:
        print(number)
