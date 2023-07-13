from earnings import *
from income import *
from models import *
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

    income_report = IncomeReport(revq, rev_growth, 
                                 epsq, eps_growth, fcfq, fcf_growth, pegq, psq)

    # build earnings report, calc forecast percentage change
    # by using getting last fiscal year's eps and rev
    earnings_report = EarningsReport(eps_est, [epsq[-1], epsy],
                                    rev_est, [revq[1], revy],
                                    eps_report, price_delta)
    
    report = CompanyReport(report_date, earnings_report, income_report)
    print(income_report)



print('start')
start = time.time()
build_report('CRWD')
end = time.time()
print('finished')
print('program took:',(end - start) * 1000, 'milliseconds')
