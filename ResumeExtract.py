import docx2txt
import PyPDF2
import os
import re
import pandas as pd
import nltk
import stanza
from nltk.tokenize import word_tokenize
from google.colab import drive # connection to Google disk
from summarizer import Summarizer

drive.mount('content')

path_to_dataset_doc = os.path.join(os.getcwd(), ' MyDrive', 'Res_1', 'docx')
stanza.download('en')
nlp = stanza.Pipeline('en')
path_to_dataset_pdf = os.path.join(os.getcwd(),' MyDrive', 'Res_1', 'pdf_new')




class ResumeExtract:
    def __init__(self):
        doc = self.read_doc(path_to_dataset_doc, path_to_dataset_pdf)
        doc['processed_text'] = self.preprocessing(doc['raw_doc'])
        data_cv = []
        for i in range(len(doc.values)):
            data_cv.append((doc.values[i][2]))


    model = Summarizer()
    def get_summary(self, text):

        try:
            sentences_quantity = self.model.calculate_optimal_k(text, k_max=10)
            return self.model(text, ratio=0.2, num_sentences=sentences_quantity)
        except Exception as e:
            print(e)
            return text



    def read_doc( self,doc_dir_name, pdf_dir_name):
        doc_dir = os.getcwd() + '/' + doc_dir_name + '/'
        doc_names = os.listdir(doc_dir)
        doc_length = len(doc_names)
        all_docs = []
        for i in range(doc_length):
            path = doc_dir + doc_names[i]

            content = docx2txt.process(path)
            content = self.get_summary(content)
            all_docs.append(content)
        pdf_dir = os.getcwd() + '/' + pdf_dir_name + '/'
        pdf_names = os.listdir(pdf_dir)
        pdf_length = len(pdf_names)
        for i in range(pdf_length):
            path = pdf_dir + pdf_names[i]
            with open(path, mode='rb') as file:
                pdf_document = PyPDF2.PdfFileReader(file)

                first_page = pdf_document.getPage(0)

                text = first_page.extractText()
                text = self.get_summary(text)
                all_docs.append(text)
        for j in range(len(pdf_names)):
            doc_names.append(pdf_names[j])

        data_cv = self.pd.DataFrame({'Doc_name': doc_names, 'raw_doc': all_docs})
        return data_cv

    def preprocessing(self, df):
        clean_corpus = []
        for i in range(0, len(df)):
            text = df[i]

            text = re.sub('[^a-zA-Z]', ' ', text)
            text = str(text).lower()
            text = nlp(text)

            text = ' '.join(text)
            clean_corpus.append(text)
        return clean_corpus


