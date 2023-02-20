import pandas as pd
import math
from sklearn.metrics.pairwise import cosine_similarity

class TF_IDF:
    def __init__(self):

        self.TF_IDF(self, df)

    def computeTF(wordDict, bagOfWords):
        tfDict = {}
        bagOfWordsCount = len(bagOfWords)
        for word, count in wordDict.items():
            tfDict[word] = count / float(bagOfWordsCount)
        return tfDict


    def computeIDF(documents):

        N = len(documents)

        idfDict = dict.fromkeys(documents[0].keys(), 0)
        for document in documents:
            for word, val in document.items():
                if val > 0:
                    idfDict[word] += 1

        for word, val in idfDict.items():
            idfDict[word] = math.log(N / float(val))
        return idfDict

    def computeTFIDF(tfBagOfWords, idfs):
        tfidf = {}
        for word, val in tfBagOfWords.items():
            tfidf[word] = val * idfs[word]
        return tfidf


    def forming_df(data):
        df = pd.DataFrame
        for i in range(len(data)):
            document = data[i]
            bagOfWords = document.split(' ')
            uniqueWords = set(bagOfWords)
            numOfWords = dict.fromkeys(uniqueWords, 0)
            for word in bagOfWords:
                numOfWords[word] += 1
            tf = computeTF(numOfWords, bagOfWords)
            idfs = computeIDF([numOfWords])
            tfidf = computeTFIDF(tf, idfs)
            job_add = pd.DataFrame([tfidf])
            job_add.head()
            df = df.append(job_add, ignore_index=True)
        return df


    def TF_IDF(df):
        score_array = []

        for i in range(48):
            score_array = score_array.append(cosine_similarity(df.index[0][i], df.index[0][49:]))

        return score_array