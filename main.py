from src.report import make_print_report, print_report
import argparse
import sys
import time

# parse the argument parser
parser = argparse.ArgumentParser(description='cli')
# add the argument
parser.add_argument('-r', '--retrieve', action='store_true', help='Increase output verbosity')
# collect the variable args
parser.add_argument('vargs', nargs=argparse.REMAINDER, help='Variable-length arguments')

# Parse the command-line arguments
args = parser.parse_args()

if __name__ == "__main__":
    # we want to retrieve from prior snapshots or build a new report
    if args.retrieve:
        print('Retrieve mode is enabled.')
        print(args.vargs)
        tickers = args.vargs
        start = time.time()
        print_report(tickers)
        end = time.time()
        print('program took:',(end - start) * 1000, 'milliseconds')
    else:
        print('Scraping new reports')
        tickers = args.vargs
        start = time.time()
        make_print_report(tickers)
        end = time.time()
        print('program took:',(end - start) * 1000, 'milliseconds')