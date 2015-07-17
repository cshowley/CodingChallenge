from os.path import join
from re import search
import time

t1 = time.time()

filename = 'tweets.txt'
words = []
numChars = 0
with open(join('./tweet_input/', filename),'rU') as data:
    tweets = data.readlines()
    for line in tweets:
        word = line.split()
        for foo in word:
            if search('\xe2\x80\x98',foo):
                foo = foo.replace('\xe2\x80\x98','\'')
            elif search('\xe2\x80\x9c',foo):
                foo = foo.replace('\xe2\x80\x9c','"')
            words.append(foo)
            if len(foo) > numChars:
                numChars = len(foo)

short = []
wordCount = {}
for word in words:
    if wordCount.has_key(word):
        wordCount[word] += 1
    else:
        wordCount[word] = 1
        short.append(word)

short.sort()

temp1 = []
temp2 = []

filename = 'ft1.txt'
template = '{0:%i} {1:10}\n' % numChars
i = 0
with open(join('./tweet_output/', filename),'w') as data:
    pass
while i < len(short):
    with open(join('./tweet_output/', filename),'a') as data:
        data.write(template.format(short[i],wordCount[short[i]]))
        temp1.append(short[i])
        temp2.append(wordCount[short[i]])
        i += 1

print time.time() - t1

print max(temp2)
print temp1[temp2.index(max(temp2))]
