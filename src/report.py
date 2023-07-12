from earnings import *
from income import *
import time

def build_report(ticker):

    # income financial report
    report_date, revq, rev_growth, epsq, eps_growth = company_income(ticker)
    fcfq, fcf_growth = company_fcf(ticker)
    pegq, psq = company_ratios(ticker)

    # earnings financial report
    eps_est, rev_est, eps_report = earnings_est(ticker)
    price_delta = price_change(ticker)

    income_report = {}
    income_report['report_date'] = report_date

    print(income_report)



print('start')
start = time.time()
build_report('CRWD')
end = time.time()
print('finished')
print('program took:',(end - start) * 1000, 'milliseconds')
