

import re
from collections import Counter
from math import log
from PorterStemmer import PorterStemmer
from Preprocess import Preprocess

# for testing

import nltk
from nltk.corpus import twitter_samples

class NaiveBayesClassifier(Preprocess):

    def __init__(self): # removing preprocess from input
        super().__init__()
        print("NaiveBayesClassifier class Initialized")

        # Class-wise counts of words
        self.class_word_counts = {}
        # Class-wise counts of documents
        self.class_doc_counts = {}
        # Set of unique words in the corpus
        self.vocab = set()
        # Total count of documents
        self.total_docs = 0
        # Preprocess instance
        self.preprocess = Preprocess()

    def train(self, documents, labels):
        for doc, label in zip(documents, labels):
            # Preprocess the document
            words = self.preprocess.lower(self.preprocess.remove_stopwords(doc))
            
            # Update class-wise counts
            if label not in self.class_word_counts:
                self.class_word_counts[label] = Counter()
            for word in words:
                self.class_word_counts[label][word] += 1
                self.vocab.add(word)
            
            if label not in self.class_doc_counts:
                self.class_doc_counts[label] = 0
            self.class_doc_counts[label] += 1
            self.total_docs += 1

    def predict(self, document):
        words = self.preprocess.lower(self.preprocess.remove_stopwords(document))
        # NOTE : Add more functions if required from the preprocess class
        class_probs = {}

        for label in self.class_doc_counts.keys():
            prior = log(self.class_doc_counts[label] / self.total_docs)
            # Laplace Smoothing, to handle zero probability
            likelihood = sum(log((self.class_word_counts[label][word] + 1) / (sum(self.class_word_counts[label].values()) + len(self.vocab))) for word in words)
            posterior = prior + likelihood
            class_probs[label] = posterior
        return max(class_probs, key=class_probs.get)


# Testing the model 

test_doc = NaiveBayesClassifier()
test_doc.train('This is good', 'Positive')

test_ds = nltk.download("twitter_samples")