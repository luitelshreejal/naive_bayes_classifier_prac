from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# emails = fetch_20newsgroups(categories = ['rec.sport.baseball', 'rec.sport.hockey']) #selects only two features since we want to measure how effective it is in telling the difference between rec.sport.baseball and rec.sport.hocket

train_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'], subset = "train", shuffle = True, random_state = 108)

test_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'], subset = "test", shuffle = True, random_state = 108)

print(test_emails.target)

# print(test_em.target_names)

# print(emails.data[5])

# print(emails.target[5]) #hockey email because it correspodonds to no. 5

counter = CountVectorizer()

counter.fit(test_emails.data + train_emails.data)

train_counts = counter.transform(train_emails.data)

test_counts = counter.transform(test_emails.data)

classifier = MultinomialNB()

classifier.fit(train_counts, train_emails.target)

print(classifier.score(test_counts, test_emails.target))
