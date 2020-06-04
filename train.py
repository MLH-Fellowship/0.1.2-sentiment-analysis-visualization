import LSTM

from keras.optimizers import RMSprop

# max sequence length of 500
# vocab size of 1000
model = LSTM.Network(500, 1000)
model.summary()
model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(), metrics=['accuracy'])