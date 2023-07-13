from income import eps_to_float

class IncomeReport(object):
    def __init__(self, revq, rev_growth, epsq, eps_growth, fcfq, fcf_growth, pegq, psq):
        self.revq = '-> '.join(revq)
        self.rev_growth = rev_growth
        epsq = [str(eps_to_float(eps)) for eps in epsq]
        self.epsq = '-> '.join(epsq)
        self.eps_growth = eps_growth
        self.fcfq = '-> '.join(fcfq)
        self.fcf_growth = fcf_growth
        self.pegq = ' <-'.join(pegq)
        self.psq = ' <-'.join(psq)

    def __str__(self):
        return str(self.__dict__)