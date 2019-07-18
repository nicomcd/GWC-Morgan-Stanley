'''
In this program, we print out all the text data from our twitter JSON file.
Please explain the comments to students as you code.
'''

# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Next we want to open the JSON file. We tag this file as
# "r" read only because we are only going to look at the data.
tweetFile = open("../Desktop/tweets_small.json", "r")

# We use the JSON library to get data from the file as JSON data.
tweetData = json.load(tweetFile)
# print(len(tweetData))
# print(list(tweetData[0].keys()))


###Find the average number of favorites per tweets with favorites != 0
favorite_count = 0
for i in range (0, len(tweetData)):
	if "favorite_count" in tweetData[i]:
		favorite_count += tweetData[i]["favorite_count"]
avg = favorite_count/len(tweetData)
# print(avg)

###create a list of all tweets with text and wordcloud
tweet_texts = []
for y in range (0, len(tweetData)):
	if "text" in tweetData[y]:
		tweet_texts.append(tweetData[y]["text".lower()])

###print the list
# print(tweet_texts)
###below is prettier list
# for z in range(0, len(tweet_texts)):
# 	print(tweet_texts[z])
tweetString = ""
for tweet in tweet_texts:
	tweet += " "
	tweetString += tweet
print(tweetString)

wordcloud = WordCloud().generate(tweetString)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
plt.savefig('nicolescloud.png')

a_counter = 0
b_counter = 0

for g in range(0, len(tweet_texts)):
	if "a" in tweet_texts[g]:
		a_counter += 1
	if "b" in tweet_texts[g]:
		b_counter += 1
# print(f"Amount of 'a' in tweets: {a_counter}.")
# print(f"Amount of 'b' in tweets: {b_counter}.")

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
# print(list_of_twitter_data)

# print(tweet_texts[0])
#
# tb = TextBlob(tweet_texts[0])
# print(tb.polarity)
# d = (len(tweetData))

# sum_likes = 0
# avg_likes = 0
# for like in range(d):
# 	sum_likes += _count
# 	avg_likes = sum_likes/d
# print(avg_likes


# print(type(tweetData))
# print(type(tweetData[1]))

# print(list(tweetData[1].keys()))
# print(tweetData[1]['text'])

# We can close the file now that we have locally stored the data.
tweetFile.close()

# We then print the data of ONE tweet:
# the [0] denotes the *first* tweet object.
# We access parts of the tweet using ["NameOfPart"].
# print("Tweet id: ", tweetData[0]["id"])

# # First ask students how they might print the text object:
# # Then show them the following code
# print("Tweet text: ", tweetData[0]["text"])


# First ask students how might they use loops
# to print the ["text"] of all the tweets:

# Show them the following two options:

# Explain how here, we're using index and
# counting the number of tweets in the tweetData
# using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])

# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])

# Encourage students to think about how there are
# often multiple solutions for each problem, and
# how each solution might have strenghts and drawbacks.
