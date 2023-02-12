#!/usr/bin/python3

import requests

def request_deletion(tweet_id):

    # The code below MUST be adapted to your own account
    # Anyway, anonymization was done (so does not compile)
    # See README   

    cookies = {
        'd_prefs': 'XXXXXXXXXXXXXX',
        '_ga': 'XXXXXXX',
        ...
        }

    headers = {
        'User-Agent': 'XXXXXXXX',
        ...
        }

    # Insert the 'tweet_id' variable here

    json_data = {
        'variables': {
            'tweet_id': tweet_id,
            'dark_request': False,
            },
        'queryId': 'YOUR-QUERY-ID',
        }

    # Add try / catch management to the original code

    try:
        response = requests.post(
            'https://api.twitter.com/graphql/<YOUR-QUERY-ID>/DeleteTweet',
            cookies=cookies,
            headers=headers,
            json=json_data,
            timeout=10
        )
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        return 500

    return response.status_code
