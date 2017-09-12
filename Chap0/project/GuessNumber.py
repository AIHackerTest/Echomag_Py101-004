cornum = 14

for i in range(1,11):

    num = input("请输入数字：")

    if i < 10 and num.isdigit() == True:
        intnum = int(num)

        if intnum > cornum:
            print("比正确答案大了")
        elif intnum < cornum:
            print("比正确答案小了")
        elif intnum == cornum and i != 10:
            print("答案正确，答案就是%d" % cornum)
            exit(0)
        else:
            print("答案正确，答案就是%d" % cornum)
            exit(0)
        print("你还有%d次机会可以输入" % (10 - i))

    elif i == 10 and num.isdigit() == True:
        if intnum > cornum:
            print("比正确答案大了")
        elif intnum < cornum:
            print("比正确答案小了")
        elif intnum == cornum and i != 10:
            print("答案正确，答案就是%d" % cornum)
            exit(0)
        else:
            print("答案正确，答案就是%d" % cornum)
            exit(0)

    elif num.isdigit() == False:
        print("请确保你输入的是数字")
        print("你还有%d次机会可以输入" % (10 - i))
