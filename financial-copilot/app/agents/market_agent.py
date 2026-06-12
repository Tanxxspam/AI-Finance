import yfinance as yf

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    return {
        "company": info.get("longName"),
        "price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "sector": info.get("sector")
    }


def market_agent(query, ticker="AAPL"):
    data = get_stock_info(ticker)

    return f"""
Company: {data['company']}
Price: {data['price']}
Market Cap: {data['market_cap']}
P/E Ratio: {data['pe_ratio']}
Sector: {data['sector']}
"""