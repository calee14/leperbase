from earnings import *
from income import *
from models import *
from util.snapshot import store_report, get_report
import time
import csv
import pandas as pd

def build_report(ticker) -> CompanyReport:
    '''
    Run scraper functions to build report and store
    it into json file.
    '''
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

def report_csv(reports: list[CompanyReport]):

    income_df = pd.DataFrame(columns=['Revenue', 'Rev. Growth', 'Earnings', 'EPS Growth', 'FCF', 'FCF Growth', 'Price/Earnings/Growth', 'Price/Sales'])
    
    income_data = {
        'Revenue': [], 
        'Rev. Growth': [], 
        'Earnings': [], 
        'EPS Growth': [], 
        'FCF': [], 
        'FCF Growth': [], 
        'Price/Earnings/Growth': [], 
        'Price/Sales': []
    }
    # build the income and earning reports for all companies
    for report in reports:
        income_report = report.income_report
        income_data['Revenue'].append(income_report.revq)
        income_data['Rev. Growth'].append(income_report.rev_growth)
        income_data['Earnings'].append(income_report.epsq)
        income_data['EPS Growth'].append(income_report.eps_growth)
        income_data['FCF'].append(income_report.fcfq)
        income_data['FCF Growth'].append(income_report.fcf_growth)
        income_data['Price/Earnings/Growth'].append(income_report.pegq)
        income_data['Price/Sales'].append(income_report.psq)
    
    income_df = pd.DataFrame(income_data)

    writer = pd.ExcelWriter('report.xlsx', engine='xlsxwriter')
    
    income_df.to_excel(writer, 
                       sheet_name='IncomeReport',
                       index=False)
    for col in income_df:
        col_len = max(income_df[col].astype(str).map(len).max(), len(col))
        col_idx = income_df.columns.get_loc(col)
        writer.sheets['IncomeReport'].set_column(col_idx, col_idx, col_len)

    # Access the workbook and worksheet objects
    workbook = writer.book
    worksheet = writer.sheets['IncomeReport']

    # Write the DataFrame to the worksheet with header formatting
    header_format = workbook.add_format({'bold': False})
    for col_num, value in enumerate(income_df.columns):
        worksheet.write(0, col_num, value, header_format)

    # Define cell formats for alternating row colors
    even_format = workbook.add_format({'bg_color': '#F4F9F8', 'align':'center', 'border': 1, 'border_color': '#929292'})
    odd_format = workbook.add_format({'bg_color': '#FFFFFF', 'align': 'center', 'border': 1, 'border_color': '#929292'})

    # Apply alternating row colors by iterating through rows
    for i, row in income_df.iterrows():
        row_format = even_format if i % 2 == 0 else odd_format
        for j, value in enumerate(row):
            worksheet.write(i+1, j, value, row_format)

    workbook.close()
    

def make_print_report(tickers: list[str]):
    reports: list[CompanyReport] = []
    for ticker in tickers:
        # builds report for ticker
        report: CompanyReport = build_report(ticker)
        reports.append(report) 
        
def test_store():
    income_report = {'revq': '487.83M -> 535.15M -> 580.88M -> 637.37M -> 692.58M', 'rev_growth': 42, 'epsq': '-0.14 -> -0.21 -> -0.24 -> -0.2 -> 0.0', 'eps_growth': 100, 'fcfq': '159.74M -> 138.25M -> 176.41M -> 212.85M -> 230.93M', 'fcf_growth': 45, 'pegq': '1.61 <- 1.22 <- 2.19 <- 3.79 <- 4.63', 'psq': '12.49 <- 12.06 <- 20.25 <- 25.68 <- 31.10'}
    earnings_report = {'eps_est': '0.51', 'eps_act': '0.57', 'eps_surprise': 11, 'eps_growth_quarter_year_forecast': [55900, 402], 'rev_growth_quarter_year_forecast': [35, 35], 'price_delta': 46}

    report = CompanyReport('CRWD', 'today', IncomeReport.load_json(income_report), EarningsReport.load_json(earnings_report))
    # print(report)

    store_report(report)
    
    report_csv([report])

print('start')
start = time.time()
# build_report('CRWD')
test_store()
# make_print_report(['CRWD'])
end = time.time()
print('finished')
print('program took:',(end - start) * 1000, 'milliseconds')
