import requests 
import sys
import argparse

parser = argparse.ArgumentParser(
        prog = 'sloworis',
        description = 'my version of slowloris'
        )

parser.add_argument('-u',action='store_const',default=None)

url = parser.parse_args(['-u'])
print(url)
