import argparse
from data.loader import load_data

parser = argparse.ArgumentParser()
parser.add_argument('city', default='default', help='location')
parser.add_argument('days', help='time period')
parser.add_argument('-m', '--method', default='api', help='data accuireing? method')
parser.add_argument('metric', nargs='?', default='aboba', help='metrics idk')
args = parser.parse_args()

def main():

    df_weather = load_data(args)


    # print(type(args))
    print(args)
    print(df_weather)
    print(df_weather.describe())


if __name__ == '__main__':
    main()
