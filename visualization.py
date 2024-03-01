import pandas as pd
import plotly.express as px
import textwrap

def plot_price_with_news(price_df: pd.DataFrame, news_headlines_df: pd.DataFrame, title: str = 'Stock price'):

    fig = px.line(
        price_df,
        x='Date',
        y='TRDPRC_1',
        width=1200,
        title=title
    )

    potential_news_df = news_headlines_df[news_headlines_df['Good news'].isin(['YES', 'NO'])]

    for i, news in potential_news_df.iterrows():
        fig.add_vline(
            x=news['date'],
            line_color='lightgrey',

        )

        if news['Good news'] == 'YES':
            annotation = 'Positive'
            bgcolor = 'lightgreen'
        else:
            annotation = 'Negative'
            bgcolor = 'pink'
            
        description = textwrap.fill(news['headline'], width=16, placeholder='...').replace('\n', '<br />')
        fig.add_annotation(
            x=news['date'], 
            y=1, 
            xref='x',
            yref='paper',
            text=annotation,
            hovertext=description,
            showarrow=True,
            arrowhead=1,
            align='left',
            bgcolor=bgcolor
        )
    return fig
