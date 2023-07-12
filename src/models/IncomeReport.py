class IncomeReport(object):
    def __init__(self, revq, rev_growth, epsq, eps_growth, pegq, psq):
        self.revq = ' '.join(revq)
        self.rev_growth = rev_growth
        self.epsq = ' '.join(epsq)
        self.eps_growth = eps_growth
        self.pegq = '<-'.join(pegq)
        self.psq = '<-'.join(psq)