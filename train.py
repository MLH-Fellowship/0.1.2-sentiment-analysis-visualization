import LSTM
import data
from keras.optimizers import RMSprop

VOCAB_SIZE = 5000
MAX_SEQ_LEN = 500

imdb = data.Dataset(MAX_SEQ_LEN, VOCAB_SIZE)
print(imdb.X_test)

model = LSTM.Network(MAX_SEQ_LEN, VOCAB_SIZE)
model.summary()
model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(), metrics=['accuracy'])
