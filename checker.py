from os.path import join

i = 0
with open(join('./tweet_output/','myway.txt'),'rU') as data:
    tweets1 = data.readlines()
    tweets1[i].strip('\n')
    i += 1

i = 0
with open(join('./tweet_output/','sort.txt'),'rU') as data:
    tweets2 = data.readlines()
    tweets2[i].strip('\n')
    i += 1

len(tweets1) == len(tweets2)

for i in range(len(tweets1)):
    if tweets1[i] != tweets2[i]:
        print i
        break


print len(tweets1),len(tweets2)
print 'done'