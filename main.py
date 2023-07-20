from src.report import make_print_report
import sys
import time

if __name__ == "__main__":
    tickers = sys.argv[1:]
    start = time.time()
    make_print_report(tickers)
    end = time.time()
    print('program took:',(end - start) * 1000, 'milliseconds')