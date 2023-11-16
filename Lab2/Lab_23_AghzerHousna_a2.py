# Deploy the model with streamlit
# Amelioration comme la publicité du deployement sur streamlit website
import streamlit as st
import yfinance as yf

st.header('Stock price prediction')
st.image('Lab2/datasets/bot.jpeg')
symbol = 'AAPL'
symbol = st.sidebar.selectbox('Select your stock symbol', ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'IAM', 'MSA'])
st.write(symbol)
start_date = st.sidebar.date_input('Start date')
end_date = st.sidebar.date_input('End date')
dataset_train = yf.download(symbol, start=start_date, end=end_date)
st.write(dataset_train)
