import pandas as pd
import yfinance as yf
import seaborn as sns

start_date = '2014-01-01'
end_date = '2024-12-31'

assets = ['ITSA4.SA','BBAS3.SA', 'TASA4.SA','SAPR4.SA']

df_data = yf.download(assets, start=start_date, end=end_date)