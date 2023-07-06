import requests
from bs4 import BeautifulSoup

# Set the headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
}

def earnings_est(ticker):

    # Set the URL of the page you want to scrape
    url = f"https://finance.yahoo.com/quote/{ticker}/analysis?p={ticker}"

    # Send a GET request to the website with headers
    response = requests.get(url, headers=headers)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # print(soup.find('div', id='Main'))
    tables = soup.find_all('table')
    
    # earnings estimate table
    earnings_rows = tables[0].find_all('tr')
    print(earnings_rows[2])

    # revenue estimate table
    revenue_rows = tables[1].find_all('tr')
    print(revenue_rows[2])

    # earnings report table
    report_rows = tables[2].find_all('tr')
    print(report_rows[1])

    

def price_change(ticker):

    # Set the URL of the page you want to scrape
    url = f"https://finance.yahoo.com/quote/{ticker}/history?period1=1672963200&period2=1688601600&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true"

earnings_est('CRWD')