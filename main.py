import argparse

parser = argparse.ArgumentParser()
parser.add_argument('city', help='location')
parser.add_argument('days', help='time period')
parser.add_argument('-m', '--method', default='html', help='data accuireing? method')
parser.add_argument('metric', nargs='?', default='aboba', help='metrics idk')
args = parser.parse_args()

def main():

    if args.__dict__['method'] == 'html':
        pass
    # data = fetch_weather("Amsterdam")
    # df = to_dataframe(data)
    #
    # stats = analyze(df)
    #
    # print(stats)
    # plot(df)
    print(type(args))


if __name__ == '__main__':
    main()
