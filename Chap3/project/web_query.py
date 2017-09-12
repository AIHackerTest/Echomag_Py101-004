from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

#国外API查询频繁会连接不上，先进行城市存在与否的判断
def get_currentweather(cityinput):
    with open('city.list.json','r', encoding="utf-8") as f:
        city = json.load(f)

    cityname = cityinput[0].upper() + cityinput[1:].lower()
    for i in range(0,len(city)):
        exist_or_not = cityname in city[i].values()
        if exist_or_not == True:
            break
    #return cityname, exist_or_not

    #从API获取城市天气信息
    #def fetchweather(cityinput):
    u = "http://api.openweathermap.org/data/2.5/weather?q={0}&units=metric&APPID={1}"
    appid = "568a6bd93f8e877585a2861d33ffec80"
    r = requests.get(u.format(cityinput,appid))
    dataload = json.loads(r.text)
    #return dataload

    #解码获取的天气信息
    #def decodeweather(dataload,cityname):
    weather = dataload['weather'][0]['description']
    temp = dataload['main']['temp']
    currentweather = "%s 天气为：%s，温度为 %d ℃" % (cityname, weather,temp)
    return currentweather

historylist = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_request')
def process_request():
    if request.args.get('help') == "帮助":
        return render_template('help.html')
    elif request.args.get('query') == "查询":
        city = request.args.get('city')
        currentweather = get_currentweather(city)
        historylist.append(currentweather)
        return render_template('query.html', currentweather=currentweather)
    elif request.args.get('history') == "历史":
        return render_template('history.html', historylist=historylist)

if __name__ == "__main__":
    app.run(debug = True, port = 8080) #使用debug模式可以在边改写，边刷新浏览器查看
