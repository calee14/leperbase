
def calculate_percentage_change(old_eps, new_eps):
    small_value = 1e-3  # A small positive value to compare against zero

    if old_eps != 0:
        percentage_change = ((new_eps - old_eps) / old_eps) * 100
    else:
        percentage_change = ((new_eps - small_value) / small_value) * 100

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
                             calculate_percentage_change(eps_prior[1], eps_est[0])]
        # calc rev growth: forecast rev next quarter v. quarter yoy
        self.rev_forecast = 0
        self.price_delta = price_delta

    def __str__(self):
        return str(self.__dict__)