from income import rev_to_int

def calculate_percentage_change(old, new):
    small_value = 1e-3  # A small positive value to compare against zero

    if old != 0:
        percentage_change = ((new - old) / abs(old)) * 100
    else:
        percentage_change = ((new - small_value) / small_value) * 100

    return int(percentage_change)

class EarningsReport(object):
    def __init__(self, eps_est, eps_prior, rev_est, rev_prior, eps_report, price_delta):
        self.eps_est = eps_report[0]
        self.eps_act = eps_report[1]
        self.eps_surprise = eps_report[2]
        # calc eps growth: forecast eps next quarter v. quarter yoy
        eps_est = [float(eps) for eps in eps_est]
        eps_prior = [float(eps) for eps in eps_prior]
        self.eps_forecast = [calculate_percentage_change(eps_prior[0], eps_est[0]),
                             calculate_percentage_change(eps_prior[1], eps_est[1])]
        # calc rev growth: forecast rev next quarter v. quarter yoy
        rev_est = [rev_to_int(rev) for rev in rev_est]
        rev_prior = [rev_to_int(rev) for rev in rev_prior]
        print(eps_est, eps_prior)
        self.rev_forecast = [calculate_percentage_change(rev_prior[0], rev_est[0]),
                             calculate_percentage_change(rev_prior[1], rev_est[1])]
        # calc price change over past 6 months
        self.price_delta = price_delta

    def __str__(self):
        return str(self.__dict__)