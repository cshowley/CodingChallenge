# Challenge 1: Calculate the total number of times each word has been tweeted.

from os.path import join

def fixPunctuation(foo, foo_replace):
    # Python interprets and prints apostrophes and quotes into the script in their UTF-8 encoding format. This interferes with the correct ascii alphabet sorting so all instances of (') and (") are manually replaced here. Assuming these characters aren't modified by the computer's default application (e.g. opening one in Mac's TextEdit changes quotes to left-handed or right-handed quotes) all can be safely changed with two .replace() functions
    foo = foo_replace('\xe2\x80\x98','\'')  # UTF-8 code for left apostrophe
    foo = foo_replace('\xe2\x80\x9c','"')   # UTF-8 code for left quote
    return foo

# Removes any words that appear more than once in the tweets to prevent double-counting
def repeatWords(words):
    uWords = []     # A list to remove any repeated words in the list 'words'
    uWords_append = uWords.append
    wordCount = {}  # Dictionary keys are words appearing in tweets.txt and the value of each key is the number of times that specific word has appeared
    wordCount_key = wordCount.has_key
    for word in words:
        if wordCount_key(word):
            wordCount[word] += 1
        else:
            wordCount[word] = 1
            uWords_append(word)
    uWords.sort()
    return uWords, wordCount

filename = 'tweets.txt'
words = []  # A list containing all tweets where each element is a word from a tweet
words_append = words.append
with open(join('./tweet_input/', filename),'rU') as tweets:
    for line in tweets:
        word = line.split()
        for foo in word:
            foo_replace = foo.replace
            foo = fixPunctuation(foo, foo_replace)
            words_append(foo)

uWords, wordCount = repeatWords(words)

# Write finalized processed data to ft1.txt
filename = 'ft1.txt'
with open(join('./tweet_output/', filename),'w') as data:
    for i in range(len(uWords)):
        data.write('%s' % uWords[i] +'\t'+ '%s\n' % wordCount[uWords[i]])
