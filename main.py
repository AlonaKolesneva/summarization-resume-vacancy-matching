from ResumeExtract import ResumeExtract
from ResumeExtractwithoutsum import ResumeExtract_withoutsum
from Job_discr import job_discription
from Okapi_withsum import Okapi_with_sum
from Okapi_withoutsum import Okapi_without_sum
from Ngrams_words_withsum import Ngrams_words_with_sum
from Ngrams_words_withoutsum import Ngrams_words_without_sum
from Ngrams_chars_withsum import  Ngrams_chars_with_sum
from Ngrams_chars_withoutsum import Ngrams_chars_without_sum
from TFIDF_with_sum import  TF_IDFs_with_sum
from TFIDF_without_sum import  TF_IDF_without_sum
from Bert_TF_IDF_with_sum import Bert_TF_IDF_with_sum
from Bert_TF_IDF_without_sum import Bert_TF_IDF_without_sum
from Bert_ngrams_char_with_sum import Bert_ngrams_char_with_sum
from Bert_ngrams_char_without_sum import Bert_ngrams_char_without_sum
from Bert_ngrams_words_with_sum import Bert_ngrams_words_with_sum
from Bert_ngrams_words_without_sum import Bert_ngrams_words_without_sum
from TFIDF_ngrams_char_with_sum import  TF_IDF_ngrams_char_with_sum
from TFIDF_ngrams_char_without_sum import TF_IDF_ngrams_char_without_sum
from TFIDF_ngrams_words_with_sum import  TF_IDF_ngrams_words_with_sum
from TFIDF_ngrams_words_without_sum import TF_IDF_ngrams_words_without_sum
from Bert_TFIDF_ngrams_char_with_sum import Bert_TF_IDF_ngrams_char_with_sum
from Bert_TFIDF_ngrams_char_without_sum import Bert_TF_IDF_ngrams_char_without_sum
from Bert_TFIDF_ngrams_words_with_sum import Bert_TF_IDF_ngrams_words_with_sum
from Bert_TFIDF_ngrams_words_without_sum import Bert_TF_IDF_ngrams_words_without_sum
from Bert_without_sum import Bert_without_sum
from Selection_cv import Select_cv


def main():
    Select_cv
    data_cv_with_sum = ResumeExtract
    data_cv_without_sum = ResumeExtract_withoutsum
    job_discr = job_discription
    okapiwithsum = Okapi_with_sum(data_cv_with_sum, job_discr)
    okapiwithoutsum = Okapi_without_sum(data_cv_without_sum, job_discr)
    ngramswordswithsum = Ngrams_words_with_sum(data_cv_with_sum, job_discr)
    ngramswordswithoutsum = Ngrams_words_without_sum(data_cv_without_sum, job_discr)
    ngramscharsdswithsum = Ngrams_chars_with_sum(data_cv_with_sum, job_discr)
    ngramscharsdswithoutsum = Ngrams_chars_without_sum(data_cv_without_sum, job_discr)
    TFIDFwithsum = TF_IDFs_with_sum(data_cv_with_sum, job_discr)
    TFIDFwithoutsum = TF_IDF_without_sum(data_cv_without_sum, job_discr)
    BertTFIDFwithsum = Bert_TF_IDF_with_sum(data_cv_with_sum, job_discr)
    BertTFIDFwithoutsum = Bert_TF_IDF_without_sum(data_cv_without_sum, job_discr)
    Bertngramscharwithsum = Bert_ngrams_char_with_sum(data_cv_with_sum , job_discr)
    Bertngramscharwithoutsum = Bert_ngrams_char_without_sum(data_cv_without_sum, job_discr)
    Bertngramswordswithsum = Bert_ngrams_words_with_sum(data_cv_with_sum, job_discr)
    Bertngramswordswithoutsum = Bert_ngrams_words_without_sum(data_cv_without_sum, job_discr)
    TFIDFngramscharwithsum  = TF_IDF_ngrams_char_with_sum (data_cv_with_sum, job_discr)
    TFIDFngramscharwithoutsum = TF_IDF_ngrams_char_without_sum(data_cv_without_sum, job_discr)
    TFIDFngramswordswithsum = TF_IDF_ngrams_words_with_sum(data_cv_with_sum, job_discr)
    TFIDFngramswordswithoutsum = TF_IDF_ngrams_words_without_sum(data_cv_without_sum, job_discr)
    BertTFIDFngramscharwithsum = Bert_TF_IDF_ngrams_char_with_sum(data_cv_with_sum, job_discr)
    BertTFIDFngramscharwithoutsum = Bert_TF_IDF_ngrams_char_without_sum(data_cv_without_sum, job_discr)
    BertTFIDFngramswordswithsum = Bert_TF_IDF_ngrams_words_with_sum(data_cv_with_sum,job_discr)
    BertTFIDFngramswordswithoutsum = Bert_TF_IDF_ngrams_words_without_sum(data_cv_without_sum,job_discr)
    Bertwithoutsum = Bert_without_sum(data_cv_with_sum, data_cv_without_sum, job_discr)





main()

