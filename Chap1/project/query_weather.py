#这是参考同学的作业做的改进版

print("这是一个天气查询小程序，可以输入城市名得到对应的天气值。")

# 读入天气数据，存储于字典中
#tbl = open("weather_info.txt", encoding="utf-8_sig")
#weather_tbl = tbl.readlines()
#weather_tbl = list(tbl) #和上面这句效果一样
#tbl.close()

weather_info = {}
history = {}

with open('d:\PythonTools\ZY.Py101-004\Chap1\project\weather_info.txt', 'r',encoding='utf-8_sig') as f:
    weather_tbl = f.readlines()

for line in weather_tbl:
    aline = line.split(',')
    city = aline[0]
    weather = aline[1]
    weather_info[city] = weather

# 天气查询
while True:
    cityinput = input("请输入指令或您要查询的城市名称： ")

    if cityinput in weather_info:
        print("%s 天气为：%s" % (cityinput, weather_info[cityinput]))
        history[cityinput] = weather_info[cityinput]

    elif cityinput == 'history':
        for histcity in history:
            print(histcity, history[histcity],end='')

    elif cityinput in ['h', 'help']:
        print('''
        \t输入城市名，查询该城市天气；
        \t输入 help，获取帮助文档；
        \t输入 history，获取查询历史；
        \t输入 quit，退出天气查询系统。
        ''')

    elif cityinput in ['quit', 'q']:
        print("历史查询记录：")
        for histcity in history:
            print(histcity, history[histcity],end='')
        break

    else:
        print("该城市不存在，请尝试其他城市或输入指令")
