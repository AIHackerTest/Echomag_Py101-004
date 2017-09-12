> 这是一个命令行模式的天气实时查询系统
> 可以查询全球的实时天气

+ 该程序基于[Weather API- OpenWeatherMap](http://openweathermap.org/)进行天气查询
+ 使用方法
  -  下载[城市列表](http://bulk.openweathermap.org/sample/city.list.json.gz)，解压后将之与该程序放在同一路径下；
  -  打开终端，输入 `python3 query_weather_timely.py`即可打开程序。
  -  输入城市名称的拼音后回车，得到当前查询城市的天气状况；输入拼音大小写皆可。（由于使用国外API目前只能使用拼音查询，中文输入在进一步探索中）
  -  查看历史记录：输入`history`后回车；
  -  退出程序：输入`quit`后回车；
  -  查看帮助文档：输入`h`后回车
  ```
  输入城市名，查询该城市天气；
  输入 help，获取帮助文档；
  输入 history，获取查询历史；
  输入 quit，退出天气查询系统。
  ```
