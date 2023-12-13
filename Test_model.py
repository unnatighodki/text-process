import os
import math
import PorterStemmer
import Preprocess
from  NaiveBayes import NaiveBayesClassifier
from ModelEval import ModelEvalution

# Reading the Twitter dataset
data_tweets = 'Twitter_Data.csv'
docs = []
label = []

with open(data_tweets) as file: # import twitter dataset
    tweets = file.readlines()
    #print(tweets[1:5])
    for tweet in tweets[1:10000]:
        file_csv = tweet.split(",")
        print(file_csv)

        if len(file_csv) == 2 and file_csv[0] != '"':
            docs.append(file_csv[0])
            label.append(file_csv[1].strip('\n'))


print('Total Number of tweets in the sample is: ',len(docs))

# Testing the Porter Stemmer - reduces the words to its base by removing different suffixes

test_stem = PorterStemmer()
print(test_stem.stem(docs[0])) # Getting the root
print(test_stem.get_base(docs[0], 'ess')) # Getting the base of the word by removing specific suffix

# Testing the Preprocess class methods

test_prepro = Preprocess()
print(test_prepro.remove_stopwords(docs[0]))
print(test_prepro.remove_stopwords(docs[27]))

print(test_prepro.preprocess_document(docs[54]))

# Splitting the training and testing dataset

split_num = math.floor(len(docs)*0.6)

train_x = docs[:split_num]
train_y = label[:split_num]

test_x = docs[split_num:]
test_y = label[split_num:]


# Fitting the implemented Naive Bayes Model

test_model = NaiveBayesClassifier()
test_model.train(train_x,train_y)

y_train_pred = test_model.predict(train_x) # compare with train_y
y_test_pred = test_model.predict(test_x) # compare with test_y

# Model evaluation
test_model_eval = ModelEvalution(y_actual=test_y,y_pred=y_test_pred)
test_model_eval.model_accuracy(test_y, y_test_pred)
conf_matrix = test_model_eval.conf_mat()

conf_mat = test_model_eval.dataframe_conf_mat(conf_matrix)
test_model_eval.class_precision(conf_mat,2)
test_model_eval.class_recall(conf_mat,2)

test_model_eval.f1_score(conf_mat,2)















