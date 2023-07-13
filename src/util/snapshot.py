from models.CompanyReport import CompanyReport
import json
def store_report(report: CompanyReport):
    with open('snapshot.json') as f:
        snapshots = json.load(f)
        print(snapshots)