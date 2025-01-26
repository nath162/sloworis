import requests 
import sys
import argparse

parser = argparse.ArgumentParser(
        prog = 'sloworis',
        usage = 'Slowloris DDOs technique',
        description = 'my version of slowloris',
        prefix ='--',
        argument_default = None,
        exit_on_error = True
        )

parser.add_argument('--u',action='store_const',default=None)

url = parser.parse_args(['--u'])
print(url)
