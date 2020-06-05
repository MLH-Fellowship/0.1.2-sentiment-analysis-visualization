from keras.layers import Activation
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Embedding
from keras.layers import Input
from keras.layers import LSTM
from keras.models import Sequential

def Network(max_seq_len, vocab_size):
    model = Sequential()
    model.add(Embedding(vocab_size, 64, input_length=max_seq_len))
    model.add(LSTM(64, return_sequences = True))
    model.add(Dropout(0.5))
    model.add(LSTM(64))
    model.add(Dense(256, name='FC1'))
    model.add(Dropout(0.5))
    model.add(Dense(1, name='out_layer'))
    model.add(Activation('sigmoid'))
    return model
