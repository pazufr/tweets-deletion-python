#!/usr/bin/python3

from tempfile import NamedTemporaryFile
from datetime import datetime
from tweet_request import request_deletion
import os, sys, string
import csv, shutil, time

filename='tweets_to_delete.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False)

fields = ['id', 'done']

# the period between 2 deletion requests
wait_between=2

tobeprocessed = True

with open(filename, 'r') as csvfile, tempfile:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    writer = csv.DictWriter(tempfile, fieldnames=fields)
    for row in reader:
       if tobeprocessed and row['done'] == "":
            try :
                res = request_deletion(row['id'])
                if res == 200:
                    row['done'] = datetime.now()
                    print('Processed tweet:', row['id'])
                else:
                    tobeprocessed = False
                    print('Stopped:', res)
            except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")
                raise
            time.sleep(wait_between)
       writer.writerow(row)

shutil.move(tempfile.name, filename)
