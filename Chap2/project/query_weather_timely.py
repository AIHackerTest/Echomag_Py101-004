#导入模块
import requests
import json

#使用Weather API- OpenWeatherMap
#u = "http://api.openweathermap.org/data/2.5/weather?q={0}&units=metric&APPID={1}"

#reguest.get示例
#r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&APPID=568a6bd93f8e877585a2861d33ffec80")


#国外API查询频繁会连接不上，先进行城市存在与否的判断
def judgecity(cityinput):
    with open('city.list.json','r', encoding="utf-8") as f:
        city = json.load(f)

    cityname = cityinput[0].upper() + cityinput[1:].lower()
    for i in range(0,len(city)):
        exist_or_not = cityname in city[i].values()
        if exist_or_not == True:
            break
    return cityname, exist_or_not

#从API获取城市天气信息
def fetchweather(cityinput):
    u = "http://api.openweathermap.org/data/2.5/weather?q={0}&units=metric&APPID={1}"
    appid = "568a6bd93f8e877585a2861d33ffec80"
    r = requests.get(u.format(cityinput,appid))
    dataload = json.loads(r.text)
    return dataload

#解码获取的天气信息
def decodeweather(data,cityname):
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    currentweather = "%s 天气为：%s，温度为 %d ℃" % (cityname, weather,temp)
    return currentweather

print("这是一个天气查询小程序，可以输入城市名得到对应的天气值。")

history = []

while True:
    cityinput = input("请输入指令或您要查询的城市名称的【拼音】，例如Beijing或beijing： ")
    cityname, exists = judgecity(cityinput)

    if exists == True:
        data = fetchweather(cityname)
        currentweather = decodeweather(data, cityname)
#        print("%s 天气为：%s，温度为 %d ℃" % (cityname, weather,temp))
        print(currentweather)
        history.append(currentweather)

    elif cityinput == 'history':
        for histrecord in history:
            print(histrecord)

    elif cityinput in ['h', 'help']:
        print('''
        \t输入城市名，查询该城市天气；
        \t输入 help，获取帮助文档；
        \t输入 history，获取查询历史；
        \t输入 quit，退出天气查询系统。
        ''')

    elif cityinput in ['quit', 'q']:
        print("历史查询记录：")
        for histrecord in history:
            print(histrecord)
        break

    else:
        print("该城市不存在，请尝试其他城市或输入指令，查看帮助请输入‘h’")
