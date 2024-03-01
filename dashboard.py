import pandas as pd
import streamlit as st

from visualization import plot_price_with_news

# Load data
price_df = pd.read_csv('dataset/historical_pricing.csv', parse_dates=['Date'])
news_headlines_df = pd.read_csv('dataset/news_headline.csv', parse_dates=['date'])
news_headlines_sentiment_df = pd.read_csv('dataset/news_headline_sentiment.csv', parse_dates=['date'])

# Prepare data

## news table
news_headlines_sentiment_df['date'] = news_headlines_sentiment_df['date'].dt.date
news_headlines_sentiment_df['sentiment'] = news_headlines_sentiment_df['Good news'].map({'YES': 'Positive', 'NO': 'Negative', 'UNKNOWN': 'Neutral'})

# Plot
st.write('# Raw news data')
st.dataframe(news_headlines_df, width=1600, height=400)

st.write('# Sentiment analysis using OpenAI')
def highlight_sentiment(val):
    if val == 'Positive':
        color = 'lightgreen'
    elif val == 'Negative':
        color = 'pink'
    else:
        color = ''
    return f'background-color: {color}'
st.dataframe(
    news_headlines_sentiment_df[['date', 'headline', 'sentiment', 'Elaborate']].style.applymap(highlight_sentiment), 
    width=1600, 
    height=400,
    use_container_width=True
)

st.write('# Sentiment Signal')
price_figure = plot_price_with_news(price_df, news_headlines_sentiment_df.sample(frac=0.5, random_state=6), title='Stock price: PTT')
st.plotly_chart(price_figure, use_container_width=True)