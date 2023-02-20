import re
from nltk.util import ngrams
from sklearn.feature_extraction.text import CountVectorizer
import numpy


class N_GRAMS_CHARS:
    def __init__(self):

        self.for_cos_array(self, data_cv, job_discr)

    def get_ngrams(text_list):
        for text in text_list:
            text = text_list.only_words(text)
        vectorizer = CountVectorizer(ngram_range=(1, 1))
        vector = vectorizer.fit_transform(text_list)
        vectorizer.get_feature_names_out()
        return vector.toarray()

    def only_words(text):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
        return text

    def calcute_cosine(cv, jb):

        cosine = numpy.dot(cv, jb)
        return cosine

    def for_cos_array(cv, jb):
        job_array = []
        for i in range(len(jb)):
            ja = cv.calcute_cosine(cv, jb[i])
            job_array.append(ja)
        return job_array