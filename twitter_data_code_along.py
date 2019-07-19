import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

tweetFile = open("../GirlsWhoCode-2019-Morgan-Stanley-NYC/tweets_small.json", "r")

tweetData = json.load(tweetFile)
# print(len(tweetData))
# print(list(tweetData[0].keys()))


###Find the average number of favorites per tweets with favorites != 0
favorite_count = 0
for i in range (0, len(tweetData)):
	if "favorite_count" in tweetData[i]:
		favorite_count += tweetData[i]["favorite_count"]
avg = favorite_count/len(tweetData)
"print(avg)"

###create a list of all tweets with text
tweet_texts = []
for y in range (0, len(tweetData)):
	if "text" in tweetData[y]:
		tweet_texts.append(tweetData[y]["text".lower()])

###print the list
"print(tweet_texts)"
###below is prettier list
'''for z in range(0, len(tweet_texts)):
print(tweet_texts[z])'''

def wordCount(tweetstring, string1):
	counter = 0
	string1 = string1.lower()
	wordList = tweetstring.split(' ')
	for item in wordList:
		if item == string1:
			counter += 1
	return counter

wordCountList = []
for item in tweet_texts:
	wordoccurrences = wordCount(item, "the")
	wordCountList.append(wordoccurrences)
print(wordCountList)

plt.hist(wordCountList)
# print(min(wordCountList)), (max(wordCountList))
plt.show()

#combines values into big string
tweetString = ""
for tweet in tweet_texts:
	tweet += " "
	tweetString += tweet
# print(tweetString)

#wordcloud stuff
'''
wordcloud = WordCloud(height = 1000, width = 1000).generate(tweetString)
plt.figure(figsize = (10,10), facecolor = None)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")'''
# plt.show()
# plt.savefig('nicolescloud.png')


def countLetter(string, letter):
	counter = 0
	for let in string:
		if let.lower() == letter:
			counter += 1
	return counter

alpha = ['a', 'g', 'v', 'j', 'o', 'y', 'b', 'w', 'u', 'x', 'n', 'r', 'p', 'f', 'k', 't', 'z', 'e', 'i', 'm', 'c', 'l', 'h', 'q', 'd', 's']
letters = sorted(alpha)

occurrences = []
for letter in letters:
	occurrences.append(countLetter(tweetString, letter))
	# print(f"Letter:{letter} Occurrences:{countLetter(tweetString, letter)}!")

plt.hist(occurrences)
# print(min(occurrences)), (max(occurrences))
# plt.show()

polarities_list = []
for x in range(0, len(tweet_texts)):
	tweet_text = TextBlob(tweet_texts[x])
	polarities_list.append(tweet_text.polarity)
# print(polarities_list)


##make tweetsData[i]['id']
list_of_twitter_data = []
for i in range(0, len(tweetData)):
	tempdictionary = {}
	tempdictionary["id"] = tweetData[i]["id"]
	tempdictionary["polarity"] = polarities_list[i]
	tempdictionary["text"] = tweet_texts[i]
	list_of_twitter_data.append(tempdictionary)

###Histogram
plt.hist(polarities_list)
# print(min(polarities_list)), (max(polarities_list))
plt.xlabel('Tweets')
plt.ylabel('Sentiment')
plt.title('Histogram of Sentiment')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([-0.55, 1.05, 0.0, 75])
# plt.show()

'''
# sum_likes = 0
# avg_likes = 0
# for like in range(d):
# 	sum_likes += _count
# 	avg_likes = sum_likes/d
# print(avg_likes
'''

# print(type(tweetData))
# print(type(tweetData[1]))


# We can close the file now that we have locally stored the data.
tweetFile.close()
