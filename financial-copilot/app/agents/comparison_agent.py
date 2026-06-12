import yfinance as yf


def get_company_metrics(ticker):

    stock = yf.Ticker(ticker)
    info = stock.info

    return {
        "name": info.get("longName"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "sector": info.get("sector"),
        "price": info.get("currentPrice")
    }


def comparison_agent(ticker1, ticker2):

    company1 = get_company_metrics(ticker1)
    company2 = get_company_metrics(ticker2)

    return f"""
=== COMPANY COMPARISON ===

{company1['name']}
Price: {company1['price']}
Market Cap: {company1['market_cap']}
PE Ratio: {company1['pe_ratio']}
Sector: {company1['sector']}

--------------------------------

{company2['name']}
Price: {company2['price']}
Market Cap: {company2['market_cap']}
PE Ratio: {company2['pe_ratio']}
Sector: {company2['sector']}
"""