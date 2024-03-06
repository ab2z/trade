import alpaca_trade_api as tradeapi
import talib as ta
import alpha_test
api_key = "PKQWFVE5KI7I2RJGE7EI"
api_secret = "oTP0D7CDhkSIonorFb7RcVWV2mCfgRNpJxdenybj"
api = tradeapi.REST(api_key,
api_secret,
"https://paper-api.alpaca.markets")

account = api.get_account()
if account.trading_blocked:
    print('Account is currently restricted from trading.')
print('${} is available as buying power.'.format(account.buying_power))

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame

client = StockHistoricalDataClient(api_key,api_secret)

request_params = StockBarsRequest(
                        symbol_or_symbols=["CHPT"],
                        timeframe=TimeFrame.Day,
                        start="2022-01-01 00:00:00"
                 ) 
bars = client.get_stock_bars(request_params)
bars_df = bars.df
print(bars_df)
bars_df.columns
bars_df['MA'] = ta.SMA(bars_df['close'],timeperiod=5)
bars_df['MA']

