
import re
from collections import Counter
from math import log
from PorterStemmer import PorterStemmer


class Preprocess(PorterStemmer):
    def __init__(self):
        super().__init__()
        print("Preprocess class Initialized")

    def hashtags(self, text):
        hash_tags = re.findall(r"#(\w+)", text)
        return hash_tags
    
    def remove_users(self, tweet):
        tweet = re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet)
        return tweet
    
    def remove_links(self, tweet):
        tweet = re.sub(r'http\S+', '', tweet) 
        tweet = re.sub(r'bit.ly/\S+', '', tweet) 
        tweet = tweet.strip('[link]')
        return tweet
    
    def clean_html(self, text):
        html = re.compile('<.*?>')
        return html.sub(r'', text)
    
    def non_ascii(self, s):
        return "".join(i for i in s if ord(i) < 128)
    
    def lower(self, text):
        return text.lower()
    
    def remove_stopwords(self, text):
        cached_stopwords = set("""
            i me my myself we our ours ourselves you your yours yourself yourselves he him his himself
            she her hers herself it its itself they them their theirs themselves what which who whom
            this that these those am is are was were be been being have has had having do does did
            doing a an the and but if or because as until while of at by for with about against
            between into through during before after above below to from up down in out on off
            over under again further then once here there when where why how all any both each
            few more most other some such no nor not only own same so than too very s t can will
            just don should now
        """.split())
        #text_str = ' '.join(text)
        cached_stopwords.update(('and', 'I', 'A', 'http', 'And', 'So', 'arnt', 'This', 'When', 'It', 'many', 'Many', 'so', 'cant', 'Yes', 'yes', 'No', 'no', 'These', 'these', 'mailto', 'regards', 'ayanna', 'like', 'email'))
        new_text = ' '.join([word for word in text.split() if word not in cached_stopwords])
        return new_text
    
    def email_address(self, text):
        email = re.compile(r'[\w\.-]+@[\w\.-]+')
        return email.sub(r'', text)
    
    def remove_digits(self, text):
        pattern = r'[^a-zA-z.,!?/:;\"\'\s]'
        return re.sub(pattern, '', text)
    
    def remove_special_characters(self, text):
        pat = r'[^a-zA-z0-9.,!?/:;\"\'\s]'
        return re.sub(pat, '', text)
    
    def preprocess_document(self, document):
        # Apply preprocessing steps
        document = self.remove_users(document)
        document = self.remove_links(document)
        document = self.clean_html(document)
        document = self.non_ascii(document)
        document = self.lower(document)
        document = self.remove_stopwords(document)
        document = self.email_address(document)
        document = self.remove_digits(document)
        document = self.remove_special_characters(document)

        # Apply Porter Stemmer
        document = self.stem(document)
        return document


if __name__ == "__main__":
    doc_clean = Preprocess()
    doc_clean.preprocess_document('My Name is Lane. You can reach me via abc@gmail.com!') #