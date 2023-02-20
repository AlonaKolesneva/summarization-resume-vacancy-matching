import docx2txt
import sys
import os
import hashlib
from langdetect import detect
import PyPDF2


def chunk_reader(fobj, chunk_size=1024):
    #Generator that reads a file in chunks of bytes
    while True:
        chunk = fobj.read(chunk_size) # getting size by which reading file
        if not chunk:
            return
        yield chunk
#check files by similar hashs
def check_for_duplicates(paths, hash=hashlib.sha1):
    hashes = {}
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                hashobj = hash()#creat hash
                for chunk in chunk_reader(open(full_path, 'rb')):
                    hashobj.update(chunk) #coolect hash from files
                file_id = (hashobj.digest(), os.path.getsize(full_path))
                duplicate = hashes.get(file_id, None) # getting duplicate
                if duplicate:
                    print ("Duplicate found: %s and %s" % (full_path, duplicate))
                    os.remove((full_path, duplicate)) # delete duplicate
                else:
                    hashes[file_id] = full_path

    if sys.argv[1:]:
        check_for_duplicates(sys.argv[1:])

    else:
        print ("Please pass the paths to check as parameters to the script")


# check .doc files by language
def langcheck_doc(folder):
    document_list = []
    for path, subdirs, files in os.walk(folder):
        for name in files:
            document_list.append(os.path.join(path, name))

    for i in range(len(document_list)):
        if (detect((docx2txt.process(document_list[i]))) == 'en'): # define what text's language, and decision delete this or not

            print(1)
        else:
            os.remove(document_list[i])


# check .pdf files by language
def langcheck_pdf(folder):
    document_list = []
    for path, subdirs, files in os.walk(folder):
        for name in files:
            document_list.append(os.path.join(path, name))
    for i in range(len(document_list)):

        with open(document_list[i], mode='rb') as file:
            pdf_document = PyPDF2.PdfFileReader(file)

            first_page = pdf_document.getPage(0)

            text = first_page.extractText()
        if (detect(((text))) == 'en'):  # define what text's language, and decision delete this or not
            print(1)
        else:
            os.remove(document_list[i])



