from os.path import join
from sortedcontainers import SortedList

# Calculate the median based on the previously sorted list of words
def calculateMedian(words, numWords):
    if numWords%2 == 0:
        mid = numWords/2
        median = ((words[mid]+words[mid-1])/2.0)
    else:
        mid = (numWords-1)/2
        median = words[mid]
    return median

# Read raw tweet data into script, this time preserving each full tweet rather than parse each word as was done in numWords.py
filename = 'tweets.txt'
i = 0
with open(join('./tweet_input/', filename),'rU') as data:
    tweets = data.readlines()
    for line in tweets:
        tweets[i] = line.strip('\n')
        i += 1

# Create output file ft2.txt
filename = 'ft2.txt'
uniqueCount = {}
uCount = uniqueCount.has_key
with open(join('./tweet_output/', filename), 'w') as data:
    
    uWords = SortedList([])            # Number of unique words per tweet, will increase until its length is equal to the length of 'tweets' list
    uWords_add = uWords.add
    for tweet in tweets:
    
        tweet = tweet.split()
        
        uniqueCount = {}    # Create a new dictionary for each tweet and overwrite the dictionary from the previous iteration of the loop. Each dictionary key is a unique word from the current tweet with a null value
        for word in tweet:
            if uCount(word):
                pass
            else:
                uniqueCount[word] = 1
        foo = float(len(uniqueCount))
        
        uWords_add(foo)
        numWords = len(uWords)
        median = calculateMedian(uWords, numWords)

        data.write('%s\n' % median)

