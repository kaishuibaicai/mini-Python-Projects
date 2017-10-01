from nltk.stem import SnowballStemmer

mytext = 'hello world.'
#print (my(mytext,''))
en_stemmer = SnowballStemmer('french')
print(en_stemmer.stem(mytext))