import argparse
import requests
import pandas as pd
import json


API_KEY = "c4beee2a4cb9972e23ddb33e3d9aaf2a" # спрятать потом в env

lat = 33.44 # (-90; 90)
lon = -94.04 # (-180; 180)

def load_data(args: argparse.Namespace):
    if args.method == 'api':
        raw = load_from_site(args)
        return to_dataframe(raw)

    if args.method == 'file':
        pass

    raise ValueError('Method not implemented')


def load_from_site(args: argparse.Namespace):
    urls = {
        'cur': "https://api.open-meteo.com/v1/forecast?"
                "latitude=52.52&longitude=13.41"
                "&daily=temperature_2m_max,temperature_2m_min"
                "&hourly=temperature_2m,wind_speed_10m"
                "&timezone=auto",
        'city': f"https://geocoding-api.open-meteo.com/v1/search?name={args.city}",
        'history': ''
    }
    if args.city == 'default':
        req = requests.get(urls['cur']).json()
    else:
        req = requests.get(urls['city']).json()
    # print('-----------------------') debug response
    print(json.dumps(req, indent=4))
    # print('-----------------------')
    return req

def to_dataframe(data):
    # return pd.DataFrame(data)

    try:
        return pd.DataFrame(data['hourly'])
    finally:
        return pd.DataFrame(data)