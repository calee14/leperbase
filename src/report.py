from earnings import *
from income import *
from models import *
from util.snapshot import store_report, get_report
import time

def build_report(ticker):

    # income financial report
    report_date, revq, rev_growth, epsq, eps_growth = company_income(ticker)
    fcfq, fcf_growth = company_fcf(ticker)
    pegq, psq = company_ratios(ticker)
    revy, epsy = prior_annual_stats(ticker)

    # earnings financial report
    eps_est, rev_est, eps_report = earnings_est(ticker)
    price_delta = price_change(ticker)

    
    income_report = IncomeReport()
    income_report.load_data(revq, rev_growth, 
                            epsq, eps_growth, fcfq, fcf_growth, pegq, psq)

    # build earnings report, calc forecast percentage change
    # by using getting last fiscal year's eps and rev
    earnings_report = EarningsReport()
    earnings_report.load_data(eps_est, [epsq[-1], epsy],
                              rev_est, [revq[1], revy],
                              eps_report, price_delta)
    
    report = CompanyReport(ticker, report_date, income_report, earnings_report)
    
    store_report(report)

    return report
    
def test_store():
    income_report = {'revq': '487.83M -> 535.15M -> 580.88M -> 637.37M -> 692.58M', 'rev_growth': 42, 'epsq': '-0.14 -> -0.21 -> -0.24 -> -0.2 -> 0.0', 'eps_growth': 1.0, 'fcfq': '159.74M -> 138.25M -> 176.41M -> 212.85M -> 230.93M', 'fcf_growth': 45, 'pegq': '1.61 <- 1.22 <- 2.19 <- 3.79 <- 4.63', 'psq': '12.49 <- 12.06 <- 20.25 <- 25.68 <- 31.10'}
    earnings_report = {'eps_est': '0.51', 'eps_act': '0.57', 'eps_surprise': 11, 'eps_growth_quarter_year_forecast': [55900, 402], 'rev_growth_quarter_year_forecast': [35, 35], 'price_delta': 46}

    report = CompanyReport('CRWD', 'today', IncomeReport.load_json(income_report), EarningsReport.load_json(earnings_report))
    # print(report)

    store_report(report)
    
    get_report('CRWD').income_report.rev_growth

print('start')
start = time.time()
# build_report('CRWD')
test_store()
end = time.time()
print('finished')
print('program took:',(end - start) * 1000, 'milliseconds')
