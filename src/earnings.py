import requests
from bs4 import BeautifulSoup

# Set the headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
}

def percent_to_int(string):
    return round(int(string.split('.')[0]))

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
    
    # print(earnings_rows[2])

    # revenue estimate table
    revenue_rows = tables[1].find_all('tr')
    revenue_forecast = [r.get_text() for r in revenue_rows[2].find_all('td')]
    # get revenue forecast for next quarter
    rev_nq = revenue_forecast[1]
    # get revenue forecast for full year (current fiscal year)
    rev_end_yr = revenue_forecast[3]
    print(rev_nq, rev_end_yr)

    # earnings report table
    report_rows = tables[2].find_all('tr')
    # get eps estimate for the recent quarter
    report_eps_est = report_rows[1].find_all('td')[-1].get_text()
    # get eps actual for recent quarter
    report_eps_act = report_rows[2].find_all('td')[-1].get_text()
    # get eps surprise %
    report_eps_surprise = report_rows[4].find_all('td')[-1].get_text()
    print(report_eps_est, report_eps_act, percent_to_int(report_eps_surprise))

    

def price_change(ticker):

    # Set the URL of the page you want to scrape
    url = f"https://finance.yahoo.com/quote/{ticker}/history?period1=1672963200&period2=1688601600&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true"

earnings_est('CRWD')