"""weather in city"""

import python_weather
import asyncio
import os


def f_to_cel(f):
    return round((f - 32) / 9*5, 2)


async def getweather(city):
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:
        weather = await client.get(city)
        print(f"Weather in {city}:  {f_to_cel(forecast.date, forecast.astronomy)} ℃")
    
        for forecast in weather.forecasts:
            print
        
            for hourly in forecast.hourly:
                print(f" --> {hourly!r}")
 

if os.name == "nt":

    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())

city = input("Input city name: ")
asyncio.run(getweather(city))

