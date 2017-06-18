#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import json
import re
import datetime
today = datetime.date.today()

APIKEY = None
with open('./APIKEY', 'r') as f:
    APIKEY = f.read().strip()

def getWeather() :
    city_id = 1850147
    unit_style = "metric"
    api_url = "http://api.openweathermap.org/data/2.5/forecast"
    api_param = { 'id': city_id, 'units': unit_style, 'APPID': APIKEY }
    
    # fetch weather data from Livedoor weather API

    r = requests.get(api_url, params=api_param)
    res = json.loads(r.content)

    # Get todays forecast
    skeleton = {'clouds': {'all': 0}, 'rain': {'3h': 0.0}, 'sys': {'pod': 'z'}, 'dt_txt': '1990-01-01 00:00:00', 'weather': [{'main': '', 'id': 0, 'icon': '', 'description': ''}], 'dt': 0, 'main': {'temp_kf': 0.0, 'temp': 0.0, 'grnd_level': 0.0, 'temp_max': 0.0, 'sea_level': 0.0, 'humidity': 0, 'pressure': 0.0, 'temp_min': 0.0}, 'wind': {'speed': 0.0, 'deg': 0.0}}
    forecasts = { 'hr09': skeleton, 'hr12': skeleton, 'hr15':skeleton, 'hr18': skeleton, 'hr21': skeleton }
    today_date = today.isoformat()
    today_date = "2017-06-18"

    echowords = ["today_weather_is"]
    for dp in res[u'list'] :
        dpdate = datetime.datetime.fromtimestamp(dp[u'dt']).strftime("%Y-%m-%d")
        if dpdate == today.strftime("%Y-%m-%d") :

            print "%s matches at %s" % ( today_date, dp[u'dt_txt'] ) 

            # hour
            hour = datetime.datetime.fromtimestamp(dp[u'dt']).strftime("%H")
            echowords.append("hr%s" % hour )

            # weather
            wth = dp[u'weather'][0][u'main']
            wth_d = dp[u'weather'][0][u'description']
            if   wth == "Clear" or wth_d == "few clouds" : echowords.append("wth_sunny")
            elif wth == "Clouds" : echowords.append("wth_cloudy")
            elif wth == "Rain"   : echowords.append("wth_rainy")
            elif wth == "Drizzle": echowords.append("wth_rainy")
            elif wth == "Snow"   : echowords.append("wth_snowy")
            else : echowords.append("undefined").append(wth_d)

            forecasts["hr%s" % hour] = dp            
             
        else :
            print "%s not matches at %s" % ( today_date, dp[u'dt_txt'] )

    print forecasts

    # need ambrella
    if forecasts['hr09'][u'weather'][0][u'main'] == "Rain" or forecasts['hr18'][u'weather'][0][u'main'] == "Rain" :
        echowords.append("dont_forget_amb")

    return " ".join(echowords)



