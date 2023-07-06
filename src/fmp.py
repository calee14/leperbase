import fmpsdk
# Company Valuation Methods
symbol: str = "AAPL"
print(f"Company Profile: {fmpsdk.historical_earning_calendar(apikey='f1d2c9c5bee0aae70119b7cdd645cf6f', symbol=symbol)}")