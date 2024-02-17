import yfinance as yf
import pandas as pd

dataF = yf.download("EURUSD=X", start="2024-01-15", end="2024-02-14", interval='60m')
dataF.iloc[:,:]

def signal_generator(df):
    open = df.Open.iloc[-1]
    close = df.Close.iloc[-1]
    previous_open = df.Open.iloc[-2]
    previous_close = df.Close.iloc[-2]

    # Bearish pattern
    if (open>close and
        previous_open<previous_close and
        close <previous_open and
        open>=previous_close):
            return 1
    
    # Bullish pattern
    if (open<close and
        previous_open>previous_close and
        close>previous_open and
        open<=previous_close):
            return 2
    
    else:
        return 0
    
signal = []
signal.append(0)
for i in range(1,len(dataF)):
    df = dataF[i-1:i+1]
    signal.append(signal_generator(df))
# Signal_generator(data)
dataF["signal"] = signal   


print(dataF.signal.value_counts())
print(dataF.iloc[:, :])

