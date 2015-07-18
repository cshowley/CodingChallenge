from os.path import join
from re import search
import time

t1 = time.time()
# Read raw tweet data into script for processing

filename = 'tweets.txt'
words = [] # A list containing all tweets where each element is a word from a tweet
#numChars = 0
with open(join('../tweet_input/', filename),'rU') as data:
    tweets = data.readlines()
    for line in tweets:
        word = line.split()
        for foo in word:
            # Python has trouble handling apostrophes (') and quotes (") which by default are read into the 'words' array as shown in the 'search' function. This causes problems when sorting words into ASCII order so all instances of (') and (") are manually replaced here
            # ------- MAKE ME A FUNCTION -------------------
            if search('\xe2\x80\x98',foo):
                foo = foo.replace('\xe2\x80\x98','\'')
            elif search('\xe2\x80\x9c',foo):
                foo = foo.replace('\xe2\x80\x9c','"')
            # ----------------------------------------------
            words.append(foo)
            #if len(foo) > numChars:
                #numChars = len(foo)

# -------------- MAKE ME A FUNCTION ----------------------
uWords = []     # A list to remove any repeated words in the list 'words'
wordCount = {}  # Dictionary keys are words appearing in tweets.txt and the value of each key is the number of times that specific word has appeared
for word in words:
    if wordCount.has_key(word):
        wordCount[word] += 1
    else:
        wordCount[word] = 1
        uWords.append(word)

uWords.sort()
# --------------------------------------------------------

#temp1 = []
#temp2 = []

filename = 'ft1.txt'
#template = '{0:%i} {1:10}\n' % numChars
with open(join('../tweet_output/', filename),'w') as data:       # Create empty ft1.txt output file
    pass
for i in range(len(uWords)):
    with open(join('../tweet_output/', filename),'a') as data:   # Append results to ft1.txt
        data.write('%s' % uWords[i] +'\t'+ '%s\n' % wordCount[uWords[i]])
        #data.write(template.format(short[i],wordCount[short[i]]))
        #temp1.append(short[i])
        #temp2.append(wordCount[short[i]])

print time.time() - t1

#print max(temp2)
#print temp1[temp2.index(max(temp2))]
