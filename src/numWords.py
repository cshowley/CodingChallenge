from os.path import join
from re import search

def repeatWords(words):
    uWords = []     # A list to remove any repeated words in the list 'words'
    wordCount = {}  # Dictionary keys are words appearing in tweets.txt and the value of each key is the number of times that specific word has appeared
    for word in words:
        if wordCount.has_key(word):
            wordCount[word] += 1
        else:
            wordCount[word] = 1
            uWords.append(word)
    uWords.sort()
    return uWords, wordCount

# Read raw tweet data into script for processing

filename = 'tweets.txt'
words = [] # A list containing all tweets where each element is a word from a tweet
with open(join('./tweet_input/', filename),'rU') as data:
    tweets = data.readlines()
    for line in tweets:
        word = line.split()
        for foo in word:
            # Python has trouble handling apostrophes (') and quotes (") which by default are read into the 'words' array as shown in the 'search' function. This causes problems when sorting words into ASCII order so all instances of (') and (") are manually replaced here
            if search('\xe2\x80\x98',foo):
                foo = foo.replace('\xe2\x80\x98','\'')
            elif search('\xe2\x80\x9c',foo):
                foo = foo.replace('\xe2\x80\x9c','"')
            words.append(foo)


uWords, wordCount = repeatWords(words)

filename = 'ft1.txt'
with open(join('./tweet_output/', filename),'w') as data:       # Create output file ft1.txt
    for i in range(len(uWords)):
        data.write('%s' % uWords[i] +'\t'+ '%s\n' % wordCount[uWords[i]])
