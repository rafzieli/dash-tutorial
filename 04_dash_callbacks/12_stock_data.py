def fetch_financial_data(company='AMZN'):
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')

df = fetch_financial_data()
df = df.reset_index()
df = df[df.Date > '2019-01-01']
df = df[df.Date < '2020-01-01']

df.to_csv('AMZN.csv')
print()