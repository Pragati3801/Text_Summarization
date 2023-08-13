import spacy
import PyPDF2
from spacy.lang.en.stop_words import STOP_WORDS
import string
from heapq import nlargest


def summarize(pdf_file_path):
    pdf_file=open(pdf_file_path, 'rb')
    stopwords = list(STOP_WORDS)
    nlp=spacy.load('en_core_web_sm')
    pdf = PyPDF2.PdfReader(pdf_file)  
    # Get the number of pages in the PDF
    text=""
    with open("pdf_summary_file", "w+") as file:
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            text +=page.extract_text()
        len_text=str(len(text))
        doc=nlp(text)
        tokens=[token.text for token in doc]
        word_freq={}
        for word in doc:
            if word.text.lower() not in stopwords and word.text.lower() not in string.punctuation:
                if word not in word_freq.keys():
                    word_freq[word.text]=1
                else:
                    word_freq[word.text]+=1 
        max_freq= max(word_freq.values())
        for word in word_freq.keys():
            word_freq[word]=word_freq[word]/max_freq
        ##print(word_freq)
        sent_tokens=[sent for sent in doc.sents]
        sent_scores={}
        for sent in sent_tokens:
            for word in sent:
                if word.text in word_freq.keys():
                    if sent not in sent_scores.keys():
                        sent_scores[sent]=word_freq[word.text]
                    else:
                        sent_scores[sent]+=word_freq[word.text]
            
        select_len=int(len(sent_tokens)*0.1)
        print(select_len)
        summary = nlargest(select_len, sent_scores, key=sent_scores.get)
        final_summary=[word.text for word in summary]
        summary_res=' '.join(final_summary)
        len_sum=str(len(summary_res))
        res="Summary of your Document :"+"\n"+summary_res+"\n"+"Length of text before text summarization was "+len_text +"\n"+"Length of text after text summarization is "+len_sum     
        pdf_file.close()
        file.close()
        return res
    
