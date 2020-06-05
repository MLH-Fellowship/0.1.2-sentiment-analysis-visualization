from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
import pandas as pd
import string
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def preprocess(s):
    return stripPunctuation(removeBr(s.lower()))

def stripPunctuation(s):
    for c in string.punctuation + "’":
        s = s.replace(c, "")
    return s

def removeBr(s):
    return s.replace("<br /><br />", "")

class Dataset:
    def __init__(self, max_seq_len, vocab_size, dataset="imdb"):
        self.MAX_SEQ_LEN = max_seq_len
        self.VOCAB_SIZE = vocab_size

        if dataset == "imdb":
            print('Loading IMDB dataset')
            df = pd.read_csv('dataset/imdb.csv', names=["X","Y"], skiprows=1)
            
            # cast X to str and preprocess
            df['X'] = df.X.apply(str)
            df['X'] = df.X.apply(preprocess)

            X = df.X
            Y = df.Y

            # encode labels
            label_encoder = LabelEncoder()
            Y = label_encoder.fit_transform(Y)
            Y = Y.reshape(-1, 1)

            # 15/85 train test split
            self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(X, Y, test_size=0.15)

            self.tokenizer = Tokenizer(
                num_words=self.VOCAB_SIZE, oov_token="<OOV>")
            self.tokenizer.fit_on_texts(self.X_train)

            self.tokenize()
            self.pad()

            print(self.X_train[:30])
            print(self.Y_train[:30])

    def tokenize(self):
        self.X_train = self.tokenizer.texts_to_sequences(self.X_train)
        self.X_test = self.tokenizer.texts_to_sequences(self.X_test)

    def pad(self):
        self.X_train = sequence.pad_sequences(self.X_train, maxlen=self.MAX_SEQ_LEN)
        self.X_test = sequence.pad_sequences(self.X_test, maxlen=self.MAX_SEQ_LEN)
