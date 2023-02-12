# tweets-deletion-python
Some toolkits to delete massively your own tweets.
Disclaimers : 
* The code DOES NOT work as is. It requires some development skills to customize it for the build.
* It may work today but not anymore tomorrow as you-know-who asks to his teams to change everything every deux seconds :)
# Steps
1. Request you archive file to Twitter.
2. From the archiche, extract the tweets.js (and also tweets-part<n>.js files if you have a huge number of tweets) and put it (them) in the same directory as the tookits
3. Edit filter.py, which selects the tweets to delete. You need to indicate the range dates and you can indicate a string value if you want to affine your selection
4. Launching filter.py created tweets_to_delete.csv file
5. Edit/Build tweet_request.py (see details below)
6. Launch delete_tweets.py, which reads the csv file and launches the deletion requests one by one
7. At the end of the process or when an exception is properly caught, the csv file is updated by putting some run date is 'done' column. It allows to relaunch the deletion script because it will bypass the done requests.
# Build
The code has to be customized to your own account. Be careful, token / authentication are hardcoded once you have finished your customization.
Customization of the deletion process
1. Using a web browser and launching some development console to track the requests, delete manually a tweet et search the DeleteTweet request to api
2. The console should help you to get the curl command
3. Convert the curl command to python request. Curlconvert is your friend.
4. Copy paste partially the code into tweet_request.py file : The original code is standalone and we need to transform it into a module with a tweet_id as variable. The hardcoded tweet_id in your sample request has to be replaced with the tweet_id variable. The orther main change is to add some try/catch blocks to easily manage some common exceptions such as timeouts.
# Performance
* The filtering run takes a few seconds on 300 MB of JS archives
* The deletion part depends on the time you set between 2 requests. Run done on 25k. 
