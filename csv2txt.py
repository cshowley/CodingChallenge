from collections import defaultdict
import csv

tweets = defaultdict(list)
with open('./tweet_input/tweets.csv','rU') as data:
    reader = csv.DictReader(data,delimiter = ',')
    for row in reader:
        for (h,v) in row.items():
            tweets[h].append(v)

with open('moreNewData.txt','w') as data:
    pass
for i in range(len(tweets['text'])):
    with open('moreNewData.txt','a') as data:
        data.write('%s\n' % tweets['text'][i])