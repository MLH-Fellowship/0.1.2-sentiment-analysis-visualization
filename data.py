from keras.datasets import imdb
from keras.preprocessing import sequence

class Dataset:
    def __init__(self, max_seq_len, vocab_size, dataset="imdb"):
        self.MAX_SEQ_LEN = max_seq_len
        self.VOCAB_SIZE = vocab_size

        if dataset == "imdb":
            self.data = imdb.load_data(
                path="imdb.npz",  # where to cache dataset
                num_words=max_seq_len,
                skip_top=0,
                maxlen=vocab_size,
            )

        train, test = self.data
        X_train, self.Y_train = train
        X_test, self.Y_test = test

        # pad inputs
        self.X_train = sequence.pad_sequences(X_train, maxlen=self.MAX_SEQ_LEN)
        self.X_test = sequence.pad_sequences(X_test, maxlen=self.MAX_SEQ_LEN)
