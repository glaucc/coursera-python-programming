from posixpath import split
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

print(word_tokenize(text))

print(nltk.tokenize.sent_tokenize(text))

stopwords = stopwords.words("english")
new_text = []
for i in text.split():
    if i not in stopwords:
        new_text.append(i)

print(new_text)