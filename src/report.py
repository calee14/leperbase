from earnings import *
from income import *
import time

def build_report(ticker):

    # income finacial report
    revq, rev_growth, epsq, eps_growth = company_income(ticker)
    fcfq, fcf_growth = company_fcf(ticker)
    pegq, psq = company_ratios(ticker)

    # earnings financial report
    eps_est, rev_eps, eps_report = earnings_est(ticker)
    price_delta = price_change(ticker)

print('start')
start = time.time()
build_report('CRWD')
end = time.time()
print('finished')
print('program took:',(end - start) * 1000, 'milliseconds')
