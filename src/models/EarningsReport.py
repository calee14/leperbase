class EarningsReport(object):
    def __init__(self, eps_est, rev_est, eps_report, price_delta):
        self.eps_est = eps_report[0]
        self.eps_act = eps_report[1]
        self.eps_surprise = eps_report[2]
        # calc eps growth: forecast eps next quarter v. quarter yoy
        self.eps_forecast = 
        # calc rev growth: forecast rev next quarter v. quarter yoy
        self.rev_forecast = 