#!/usr/bin/python3

from datetime import datetime
import os, sys, json, locale, csv

locale.setlocale(locale.LC_ALL, 'en_US')

# Range dates (mandatory)
min_date_str='2021-01-01'
max_date_str = '2021-01-02'

# if you want to select only some specific tweets
# example : filter_string = 'Hot news:'
filter_string = ''

# List if you have several files for your tweets
# input files =['./tweets.js','./tweets-part1.js','./tweets-part2.js','./tweets-part3.js','./tweets-part4.js']
input_files = ['./tweets.js']

# Not needed updates below
output_file = './tweets_to_delete.csv'

min_date = datetime.strptime(min_date_str + ' +0000', '%Y-%m-%d %z')
max_date = datetime.strptime(max_date_str + ' +0000', '%Y-%m-%d %z')

with open(output_file,'w', newline='') as fileto:
    writer = csv.writer(fileto)
    writer.writerow(['id','done'])

fileto.close()

with open(output_file,'a', newline='') as fileto:
    writer = csv.writer(fileto)

    for input_file in input_files:

        with open(input_file, 'r', encoding='utf8') as f:
            data = f.readlines()
            # convert js file to JSON: replace first line with just '[', squash lines into a single string
            prefix = '['
            if '{' in data[0]:
                prefix += ' {'
            data =  prefix + ''.join(data[1:])
            result = json.loads(data)
        f.close()

        max_iter = len(result)

        for i in range(max_iter):
            if filter_string == "" or filter_string in result[i]['tweet']['full_text']:
                creation_date_str = result[i]['tweet']['created_at']
                try:
                    creation_date = datetime.strptime(creation_date_str, '%a %b %d %H:%M:%S %z %Y')
                    if (creation_date > min_date and creation_date < max_date):
                        tweet_id = result[i]['tweet']['id']
                        print(creation_date_str + ' : ' + tweet_id)
                        writer.writerow([tweet_id, ''])
                except Exception as err:
                    print(f"Unexpected {err=}, {type(err)=}")
                    raise
fileto.close()
