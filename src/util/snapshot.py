from models.CompanyReport import CompanyReport
import json
import os

def store_report(report: CompanyReport):
    if not os.path.exists('snapshot.json'):
        with open('snapshot.json', 'w') as file:
            json.dump({}, file)

    with open('snapshot.json', 'r') as f:
        snapshots = json.load(f)

    # print(snapshots)

    if report.ticker not in snapshots:
        snapshots[report.ticker] = {'reports': []}

    company_reports = snapshots[report.ticker]['reports']
    curr_report = snapshots[report.ticker]['reports'][-1] if len(company_reports) > 0 else None
    if curr_report == None or curr_report['date'] != report.date:
        print(report.as_dict())
        snapshots[report.ticker]['reports'].append(report.as_dict())
    else:
        print(report.ticker, 'already up to date.')

    # print(snapshots)

    with open('snapshot.json', 'w') as file:
        json.dump(snapshots, file, indent=2)