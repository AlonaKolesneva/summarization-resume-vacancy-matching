# script for checkin cv's on job titles
import PyPDF2
import os
import docx2txt
from flashtext.keyword import KeywordProcessor


class Select_cv:
    def __init__(self):
        self.key_check_doc(self, folder)
        self.key_check_pdf(self, folder)

    doc_folder = 'C:\\Users\\alkur\\Downloads\\Telegram Desktop\\text\\docx1'
    pdf_folder = 'C:\\Users\\alkur\\Downloads\\Telegram Desktop\\text\\pdf'
    f = open('C:\\Users\\alkur\\Desktop\\titles_combined.txt') # file from find-job-titles
    list_job = []
    for line in f:
        list_job.append(line.lower()) # to lowerCase

    developer_list_job = []


    for job in list_job:
        if (job.find("developer") >= 0): #find all vacancy with developer
            developer_list_job.append(job)

    developer_list_job = [line.rstrip() for line in developer_list_job] # delete \n in the end of string
    fullstack_list_job = []


    for job in list_job:
        if (job.find("full stack") >= 0): #find all vacancy with full stack
            fullstack_list_job.append(job)
    fullstack_list_job = [line.rstrip() for line in fullstack_list_job] # delete \n in the end of string

    united_list = [] # to unite lists of job
    for job in developer_list_job:
        united_list.append(job)

    for job in fullstack_list_job:
        united_list.append(job)

    keyword_processor = KeywordProcessor()
    for i in range(len(united_list)):
        keyword_processor.add_keyword(united_list[i])


        def key_check_doc(folder):
            document_list = []
            for path, subdirs, files in os.walk(folder):
                for name in files:
                    document_list.append(os.path.join(path, name))

            for i in range(len(document_list)):
                ab = print((document_list[i]))
                text = docx2txt.process(document_list[i])

                param = len(keyword_processor.extract_keywords(docx2txt.process(document_list[i])))
                if (param > 0):

                    print(1)
                else:
                    os.remove(document_list[i])


    def key_check_pdf(folder):
        document_list = []
        for path, subdirs, files in os.walk(folder):
            for name in files:
                document_list.append(os.path.join(path, name))
        for i in range(len(document_list)):

            with open(document_list[i], mode='rb') as file:
                pdf_document = PyPDF2.PdfFileReader(file)

                first_page = pdf_document.getPage(0)

                text = first_page.extractText()
                print(text)
            if (len(keyword_processor.extract_keywords(text)) > 0):
                print(1)
            else:
                os.remove(document_list[i])




    key_check_doc(doc_folder)
    key_check_pdf(pdf_folder)