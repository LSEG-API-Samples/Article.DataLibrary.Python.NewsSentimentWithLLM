# [AI-Driven Stock Insights: Analyzing Financial News with LLMs](https://developers.lseg.com/en/article-catalog/article/ai-driven-stock-insights--analyzing-financial-news-with-llms)
## Introduction
In the fast-paced world of finance, staying ahead means keeping informed of the latest news and market sentiments. With the vast amounts of data available, manual analysis is no longer viable. Here, we explore a breakthrough approach using Large Language Models (LLMs) like GPT for analyzing sentiments in financial news headlines, offering a glimpse into future investment strategies.

## Understanding LLMs and Their Role in Finance
LLMs are advanced AI tools capable of understanding and generating human-like text. By training on extensive datasets, they can interpret variation in language, making them perfect for analyzing the sentiment of financial news headlines. This method provides a more variation understanding of market sentiments, going beyond traditional analysis methods.

## The Study: A Brief Overview
Our reference study showcases LLMs' ability to categorize news headlines into positive, negative, or neutral sentiments towards stock prices. This categorization was then linked to stock market returns, revealing that LLMs could predict stock movements more accurately than previous models. This insight opens new avenues for investors to gauge market sentiment and make informed decisions.

## Pre-requisites:
- LSEG Workspace application with access to The Data Library desktop session, or Data Platform session
   - App Key (as the Desktop session is used here)
- Open AI API key (as GPT is used here)
- Python 3.9 or above
- Required libraries
   - refinitiv.data==1.5.1
   - numpy==1.23.4
   - openai==1.12.0
   - pandas==2.0.2
   - plotly==5.18.0
   - tqdm==4.66.2

## Practical Application: Analyzing Sentiments with Python
Actually, we provide Machine Readable News products with News Analytics (such as sentiment) over our Refinitiv Real-Time platform in realtime at very low latency - these products are essentially consumed by algorithmic applications as opposed to humans. Here we are trying to do a similar thing as simply as possible to illustrate the key elements without having to do this in a low latency environment but do this with the Data Library for Python instead.

For of the LSEG's Data Library, integrating LLMs into your investment strategy can be straightforward. Python, a versatile programming language, serves as the bridge.
To communicate with the LLM (GPT), we're using Chat Completions API from Open AI.

![news-sentiment-flow](https://github.com/LSEG-API-Samples/Article.DataLibrary.Python.NewsSentimentWithLLM/assets/89068039/09ef85a7-f705-46fe-84ff-2b5ebd0824d2)

## The Future of Investment Strategies
The integration of LLMs into financial analyses marks a significant shift in how investors approach market news. By offering a deeper, more nuanced understanding of market sentiments, LLMs pave the way for more sophisticated and informed investment strategies.

You could use this example as a base to improve your trading strategies. There're many things to experiment with this approach, for example, try to adjust the prompt used in the system message, or even use the streaming pricing data as a boundary to buy or sell stocks (Example: EX-1.01.03-PricingStream.ipynb).

If you're interested in these use cases or have an idea regarding this, or even have a question on this, feel free to make a post into our [Q&A Forum](https://community.developers.refinitiv.com/) so we can discuss and maybe create the new example together for the community!

## Conclusion
The fusion of LLMs and financial sentiment analysis represents a leap forward in investment technology. As we continue to refine these models and integrate them into our investment decision-making processes, the potential for improved accuracy and predictive power in stock market investments is immense. The journey has just begun, and the future looks promising for those ready to embrace these advanced tools.

## References
- Lopez-Lira, Alejandro and Tang, Yuehua, Can ChatGPT Forecast Stock Price Movements? Return Predictability and Large Language Models (April 6, 2023). Available at SSRN: https://ssrn.com/abstract=4412788 or http://dx.doi.org/10.2139/ssrn.4412788
- Open AI > Capabilities > Text generation models > Chat Completions API
- Open AI > Capabilities > Text generation models > Models
