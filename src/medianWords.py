from os.path import join
import time

t1 = time.time()

filename = 'tweets.txt'
i = 0
with open(join('./tweet_input/', filename),'rU') as data:
    tweets = data.readlines()
    for line in tweets:
        tweets[i] = line.strip('\n')
        i += 1

filename = 'ft2.txt'
with open(join('./tweet_output/', filename), 'w') as data:
    pass

uWords = []
for tweet in tweets:
    tweet = tweet.split()
    uniqueCount = {}
    for word in tweet:
        if uniqueCount.has_key(word):
            pass
        else:
            uniqueCount[word] = ''
    foo = float(len(uniqueCount))

    if not uWords == []:
        midP = len(uWords)/2
        if foo == midP:
            uWords.insert(midP, foo)
        elif foo >= uWords[-1]:
            uWords.append(foo)
        elif foo <= uWords[0]:
            uWords.insert(0, foo)
        elif foo > uWords[midP]:
            while foo > uWords[midP]:
                midP += 1
            uWords.insert(midP, foo)
        elif foo < uWords[midP]:
            while foo < uWords[midP]:
                midP -= 1
            uWords.insert(midP, foo)
    else:
        uWords.append(foo)

    if len(uWords)%2 == 0:
        mid = len(uWords)/2
        median = ((uWords[midP]+uWords[mid-1])/2.0)
    elif len(uWords) == 1:
        median = uWords[0]
    else:
        mid = (len(uWords)-1)/2
        median = uWords[mid]

    with open(join('./tweet_output/', filename), 'a') as data:
        data.write('%s\n' % median)

print time.time() - t1
