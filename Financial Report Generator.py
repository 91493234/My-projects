import requests
import time
import sys


def financeReport():
    try:
        api = 'VS5zrLt8vR3lgKfkphb3wMFGpO8ygFhz'

        #ticker information
        company_name_for_ticker = input('Enter company name: ').title()
        if company_name_for_ticker == "Google":
            company_name_for_ticker = "Alphabet"
        
        ticker_url = f"https://api.polygon.io/v3/reference/tickers?search={company_name_for_ticker}&active=true&apikey={api}"
        ticker_request = requests.get(ticker_url)
        data_for_ticker = ticker_request.json()

        # financial information
        ticker = data_for_ticker['results'][0]['ticker']
        url = f"https://api.polygon.io/vX/reference/financials?ticker={ticker}&apikey={api}"
        request = requests.get(url)
        data = request.json()

    # fetching data from url
        result = data['results'][0]
        company_name = result["company_name"]
        revenue = result["financials"]["income_statement"]["revenues"]["value"]
        expense = result["financials"]["income_statement"]["operating_expenses"]["value"]
        profit = revenue - expense
        if expense > revenue:
            loss = revenue - expense
        else:
            loss = 0
        profit_margin =(profit / revenue)* 100
        return company_name, revenue, loss, profit, profit_margin, ticker, api
    except IndexError:
        return

def stock_market(ticker,api):
    try:
        # stock price
        url =f'https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?apikey={api}'
        stock_request = requests.get(url)
        stock_data = stock_request.json()
        stock_price = stock_data['results'][0]['c']

        # market cap
        market_cap_url = f'https://api.polygon.io/v3/reference/tickers/{ticker}?apikey={api}'
        market_cap_request = requests.get(market_cap_url)
        market_cap_data = market_cap_request.json()
        market_cap = market_cap_data['results']['market_cap']

        return stock_price, market_cap
    except IndexError:
        return

def main():
    try:
        print("NOTE: Enter only USA Company")
        company_name, revenue, loss, profit, profit_margin, ticker, api = financeReport()
        stock_price, market_cap = stock_market(ticker, api)
        year = "2024-2025"

        info=f'''\n 
----------------------------------------------
    
    {company_name:^7} - {year}

----------------------------------------------
Financial Summary:
----------------------------------------------
Revenue        :    ${revenue:,}
Profit         :    {f'{profit:+}'[0]}${f'{profit:+,}'[1:]}
Loss           :    {f'{loss:-,}'[0]}${f"{loss:-,}"[1:]}
Profit Margin  :    {profit_margin:.2f}%
----------------------------------------------

Stock Market Data:
----------------------------------------------
Stock Price    :    ${stock_price:,}
Market Cap     :    {market_cap:e}
Inflation Rate :    3.0% (Not fixed value)
----------------------------------------------
            '''

        for char in info:
            sys.stdout.write(char) # sys.stdout.write(character) ye ek ek character print karega bina new line ke
            sys.stdout.flush() # system.stdout.flush() ye output ko turant terminal main dikhayega
            time.sleep(0.01) # time.sleep(time in second) ye sleep ho diye gaye time ke liye

    except TypeError:
        print("\nERROR: Company not found or API trial expired. Use apple or goole for API trial Expire! \n")
    except requests.exceptions.ConnectionError:
        print("\nNo internet connection!\n")

    
    
    
if __name__ == "__main__":
    main()