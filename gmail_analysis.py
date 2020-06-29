from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import nltk
import mail
from time import sleep

nltk.download('stopwords')

words = ["ключевые", "слова"]

regex_tok = RegexpTokenizer(r'\w+')

#  стоп-слова
stopwords = stopwords.words('russian') + [a for a in punctuation]


def text_from_email():
    while True:
        text_s = mail.real_gmail()
        sleep(0.1)


#  текст
text = [text_from_email.text_s.lower()]

tokens = regex_tok.tokenize(text)
tokens_no_sw = [token for token in tokens if token not in stopwords]

print(tokens_no_sw)


def analize(text_, words):
    num = 0
    for word in words:
        if word.lower() in text_:
            num += 1
            if num >=5:
                return text_from_email.text_s
            else:
                pass
