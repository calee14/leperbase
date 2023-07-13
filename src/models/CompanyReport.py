
class CompanyReport(object):
    def __init__(self, date, income_report, earnings_report):
        self.date = date
        self.income_report = income_report
        self.earnings_report = earnings_report

    def __str__(self):
        return str(self.__dict__)