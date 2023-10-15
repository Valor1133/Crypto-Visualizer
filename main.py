import yfinance as yf  
import streamlit as st  
from PIL import Image  
from urllib.request import urlopen 


Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Ripple = 'XRP-USD'
Bitcoin_Cash = 'BCH-USD'


BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(Bitcoin_Cash)


BTCHis = BTC_Data.history(period="max")
ETHHis = ETH_Data.history(period="max")
XRPHis = XRP_Data.history(period="max")
BCHHis = BCH_Data.history(period="max")

st.title(" Cryptocurrency Daily Prices ₿ ")
st.header("Your Dashboard ✨")

def predict(cry):
    cryHis = cry.history(period = "1mo")
    threshold = cryHis['Close'].mean()
    if cryHis['Close'].tail().mean() <= threshold:
        st.write(" ## Good time to buy.")
    else:
        st.write(' ## Not a good time to buy, wait.')

#Bitcoin
st.write(""" ## Bitcoin ($) """)
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
st.image(imageBTC)
st.line_chart(BTCHis.Close,  use_container_width=True)
predict(BTC_Data)

#Ethereum
st.write(""" ## Ethereum ($) """)
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
st.image(imageETH, use_column_width=False)
st.line_chart(ETHHis.Close,  use_container_width=True)
predict(ETH_Data)

#Ripple
st.write(""" ## Ripple ($) """)
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
st.image(imageXRP, use_column_width=False)
st.line_chart(XRPHis.Close,  use_container_width=True)
predict(XRP_Data)

#Bitcoin Cash
st.write(""" ## Bitcoin-Cash ($USD) """)
imageBCH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))
st.image(imageBCH, use_column_width=False)
st.line_chart(BCHHis.Close,  use_container_width=True)
predict(BCH_Data)