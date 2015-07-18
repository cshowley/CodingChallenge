from os.path import join
import time

t1 = time.time()

# Read raw tweet data into script, this time preserving each full tweet rather than parse each word as was done in numWords.py
filename = 'newData.txt'
i = 0
with open(join('./tweet_input/', filename),'rU') as data:
    tweets = data.readlines()
    for line in tweets:
        tweets[i] = line.strip('\n')
        i += 1


# Create output file ft2.txt
filename1 = 'myway.txt'
filename2 = 'sort.txt'
with open(join('./tweet_output/', filename1), 'w') as data:
    pass
with open(join('./tweet_output/', filename2), 'w') as data:
    pass

uWords1 = [] # Number of unique words per tweet, will increase until its length is equal to the length of 'tweets' list
uWords2 = []
for tweet in tweets:
    tweet = tweet.split()
    uniqueCount = {}    # Create a new dictionary for each tweet and overwrite the dictionary from the previous iteration of the loop. Each dictionary key is a unique word from the current tweet with a null value
    for word in tweet:
        if uniqueCount.has_key(word):
            pass
        else:
            uniqueCount[word] = 1
    foo = float(len(uniqueCount))

    # --------- MAKE ME A FUNCTION --------------
    # The list 'uWords' can be simply rearranged by uWords.sort(), but I've found that having to do that for very large numbers of tweets takes too much processing time. Given a value of unique words in a tweet, this function compares that value to the first, last, and middle indices in uWords and places it accordingly.

    if not uWords1 == []:
        midP = len(uWords1)/2
        if foo == uWords1[midP]:
            uWords1.insert(midP, foo)
        elif foo >= uWords1[-1]:
            uWords1.append(foo)
        elif foo <= uWords1[0]:
            uWords1.insert(0, foo)
        elif foo > uWords1[midP]:
            while foo > uWords1[midP]:
                midP += 1
            uWords1.insert((midP), foo)
        elif foo < uWords1[midP]:
            while foo < uWords1[midP]:
                midP -= 1
            uWords1.insert((midP+1), foo)
    else:
        uWords1.append(foo)


    # -------------------------------------------

    # ----- MAKE ME A FUNCTION ------------------
    # Calculates the median
    if len(uWords1)%2 == 0:
        mid = len(uWords1)/2
        median = ((uWords1[mid]+uWords1[mid-1])/2.0)

    elif len(uWords1) == 1:
        median = uWords1[0]
    else:
        mid = (len(uWords1)-1)/2
        median = uWords1[mid]

    # -------------------------------------------

    with open(join('./tweet_output/', filename1), 'a') as data:
        data.write('%s\n' % median)
# ----------- # ------------- # ------------ # ------------ #

    uniqueCount = {}

    for word in tweet:
        if uniqueCount.has_key(word):
            pass
        else:
            uniqueCount[word] = 1
    foo = float(len(uniqueCount))

    uWords2.append(foo)
    uWords2.sort()
    midP = len(uWords2)/2

    if len(uWords2)%2 == 0:
        mid = len(uWords2)/2
        median = ((uWords2[midP]+uWords2[mid-1])/2.0)
    elif len(uWords2) == 1:
        median = uWords2[0]
    else:
        mid = (len(uWords2)-1)/2
        median = uWords2[mid]

    with open(join('./tweet_output/', filename2), 'a') as data:
        data.write('%s\n' % median)
    

print time.time() - t1
