## text-process

This repository comprises a Python package implemented in the academic project - DS 5010 (Introduction to Programming for Data Science). This package is designed to process the textual information for labeled and unlabeled datasets. It contains several classes and methods required to process natural language throughout the Data Science project lifecycle. 

The motivation behind the implementation is the prevalence of NLP models during the era. An ability to deal with the language-like information in today's market is of utmost importance for a Data Scientist. This technique has applications in various domains, such as chatbots, virtual assistants, speech tagging, and sentiment analysis. 

The includes modules needed to perform several steps while doing an NLP project as:

### 1. PorterStemmer:
 
  This class implements the normalization technique, which aims to provide the root or base of the several derivations of a word. For example - running, runner, ran would result in "run." This consists of methods such as is_vowel, form, ends_with, contains_vowel. 
  
  ```
  def is_vowel(self, letter):
      letter = letter.lower()
      return letter in ('a', 'e', 'o', 'i', 'u')
        
  test_wrd.stem('specialize')
  # returns "Special"
  ```

### 2. Preprocess:
  
  This class processes the text before feeding it into machine learning model fitting. This plays an important role in preparing the data by removing the unwanted characters that do not contribute towards decision-making by using a model employing several functions, such as sentence_tokenizer, remove_users, remove_links, etc.

  ```
    def sentence_tokenizer(self, text):
        return re.split('(?<=\.|\?)\s', text)
        
    def remove_links(self, tweet):
        tweet = re.sub(r'http\S+', '', tweet) 
        tweet = re.sub(r'bit.ly/\S+', '', tweet) 
        tweet = tweet.strip('[link]')
        return tweet

  ```
### 3. NaiveBayes:

  This class implements Bayes' theorem, known as "naive," by assuming that the features are conditionally independent, given the label. This simple baseline algorithm is widely used in text classification. It consists of functions such as train and predict:

  ```
    def __init__(self): # removing preprocess from input
        #super().__init__()
        print("NaiveBayesClassifier class Initialized")

        # Class-wise counts of words
        self.class_word_counts = {}
        # Class-wise counts of documents
        self.class_doc_counts = {}

  ```
  
  
  
  

