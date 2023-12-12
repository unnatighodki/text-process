import numpy as np
import re
from collections import Counter
from math import log
from PorterStemmer import PorterStemmer
from Preprocess import Preprocess

# For testing
import nltk
from nltk.corpus import twitter_samples

class NGramClassifier(Preprocess):
    def __init__(self, n):
        super().__init__()
        print(f"NGramClassifier (n={n}) Initialized")
        self.n = n
        self.class_ngram_counts = {}
        self.class_doc_counts = {}
        self.vocab = set()
        self.total_docs = 0
        self.preprocess = Preprocess()
        
    def fit(self, documents, labels):
        for doc, label in zip(documents, labels):
            ngrams = self.generate_ngrams(doc, self.n)
            
            if label not in self.class_ngram_counts:
                self.class_ngram_counts[label] = Counter()
            for ngram in ngrams:
                self.class_ngram_counts[label][ngram] += 1
                self.vocab.add(ngram)
            
            if label not in self.class_doc_counts:
                self.class_doc_counts[label] = 0
            self.class_doc_counts[label] += 1
            self.total_docs += 1

    def generate_ngrams(self, text, n):
        words = self.preprocess.lower(self.preprocess.remove_stopwords(text)).split()
        ngrams = zip(*[words[i:] for i in range(n)])
        return [' '.join(ngram) for ngram in ngrams]

    def predict(self, documents):
        predictions = []

        if isinstance(documents, str):
            ngrams = self.generate_ngrams(documents, self.n)
            class_probs = {}

            for label in self.class_doc_counts.keys():
                prior = log(self.class_doc_counts[label] / self.total_docs)
                likelihood = sum(log((self.class_ngram_counts[label][ngram] + 1) /
                                    (sum(self.class_ngram_counts[label].values()) + len(self.vocab))) for ngram in ngrams)
                posterior = prior + likelihood
                class_probs[label] = posterior
            predicted_label = max(class_probs, key=class_probs.get)
            predictions.append(predicted_label)

            return predictions
        
        elif isinstance(documents, list):
            for doc in documents:
                ngrams = self.generate_ngrams(doc, self.n)
                class_probs = {}

                for label in self.class_doc_counts.keys():
                    prior = log(self.class_doc_counts[label] / self.total_docs)
                    likelihood = sum(log((self.class_ngram_counts[label][ngram] + 1) /
                                        (sum(self.class_ngram_counts[label].values()) + len(self.vocab))) for ngram in ngrams)
                    posterior = prior + likelihood
                    class_probs[label] = posterior
                predicted_label = max(class_probs, key=class_probs.get)
                predictions.append(predicted_label)

            return predictions



# Testing the model 
docs = [
    "This is a positive document.",
    "Negative sentiment detected in this one.",
    "Neutral statement for training purposes."
]

lab = [
    "Positive",
    "Negative",
    "Neutral"
]

test_docs = [
    "I am not happy.",
    "I am disappointed with the results",
    "Congratulations @Sam_Bahadur"
]



test_instance = NGramClassifier(2)
test_instance.fit(documents=docs,labels=lab)

test_instance.predict("This is a negative document.") # Negative
pred = test_instance.predict(documents=test_docs)
pred

# for testing

import nltk
from nltk.corpus import twitter_samples



nltk.download("twitter_samples")

# Referring - https://www.kaggle.com/code/piyushagni5/sentiment-analysis-on-twitter-dataset-nlp
all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

tweets = all_positive_tweets + all_negative_tweets
labels = np.append(np.ones((len(all_positive_tweets))), np.zeros((len(all_negative_tweets))))

len(tweets)
len(labels)
# split the data into two pieces, one for training and one for testing (validation set) 

train_pos = all_positive_tweets[:4000]
test_pos = all_positive_tweets[4000:]

train_neg = all_negative_tweets[:4000]
test_neg = all_negative_tweets[4000:]

train_x = train_pos + train_neg 
test_x = test_pos + test_neg

len(all_positive_tweets)
len(all_negative_tweets)

# combine positive and negative labels
train_y = np.append(np.ones((len(train_pos), 1)), np.zeros((len(train_neg), 1)), axis=0)
test_y = np.append(np.ones((len(test_pos), 1)), np.zeros((len(test_neg), 1)), axis=0)

# Print the shape train and test sets
print("train_y.shape = " + str(train_y.shape))
print("test_y.shape = " + str(test_y.shape))

