from models.CompanyReport import CompanyReport
import json
import os
import shutil

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
        snapshots[report.ticker]['reports'].append(report.as_dict())
        print('Added new report for', report.ticker)
    else:
        print(report.ticker, 'already up to date.')

    # print(snapshots)

    try:
        # Write JSON data to a temporary file
        with open('temp_snapshot.json', "w") as temp_file:
            json.dump(snapshots, temp_file)

        # Replace the original file with the temporary file
        shutil.move('temp_snapshot.json', 'snapshot.json')
        print('Successfully dumped', report.ticker, 'report JSON data into storage.')

    except Exception as e:
        print("Error occurred:", str(e))
        # Handle the error gracefully without modifying the original file

        # Cleanup the temporary file if it exists
        if os.path.exists('temp_snapshot.json'):
            os.remove('temp_snapshot.json')
    # with open('snapshot.json', 'w') as file:
    #     json.dump(snapshots, file, indent=2)