from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import LSTM
from tensorflow.keras.models import Sequential

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
