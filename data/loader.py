import argparse
import requests

def LoadData(args: argparse.Namespace):
    if args.__dict__['method'] == 'html':
        data = LoadFromSite(args)
    else:
        data = None

    return data

def LoadFromSite(args: argparse.Namespace):
    urls = {
        'cur': 'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}',
        'history': ''
    }
    req = requests.get('http://...')
    return req





# Цель:

# Научиться:
#
# получать данные
#
# класть в DataFrame
#
# считать
#
# Функции:
#
# fetch_weather()
#
# analyze()
#
# plot()