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

    income_report = {}
    income_report['report_date'] = report_date

    earnings_report = EarningsReport(eps_est, [epsq[-1], epsy],
                                    rev_est, [revq[-1], revy],
                                    eps_report, price_delta)
    print(earnings_report)



print('start')
start = time.time()
build_report('CRWD')
end = time.time()
print('finished')
print('program took:',(end - start) * 1000, 'milliseconds')
