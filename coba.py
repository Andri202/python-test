import nltk
import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

kalimat = "[MOJOK.co] Manfaat jogging setiap pagi yang pertama adalah meredakan stres. Olahraga itu seperti kode bagi tubuh untuk memproduksi hormon endorfin, agen perangsang rasa bahagia."

katadasar = stemmer.stem(kalimat)

#menghilangkan tanda baca
kalimat = katadasar.translate(str.maketrans('','',string.punctuation)).lower()

#merubah ke low case
case_folding = kalimat.lower()

#mebuat toket perkata
tokens = nltk.tokenize.word_tokenize(case_folding)

#untuk mendapatkan jumlah kemunculan dari tiap token
#kemunculan = nltk.FreqDist(tokens)
#print(kemunculan.most_common())



print(tokens)
