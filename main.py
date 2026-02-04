

def main():
    data = fetch_weather("Amsterdam")
    df = to_dataframe(data)

    stats = analyze(df)

    print(stats)
    plot(df)

--city
--days
--metric