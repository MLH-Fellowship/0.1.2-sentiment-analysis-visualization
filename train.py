import LSTM
import data
from keras.optimizers import RMSprop

VOCAB_SIZE = 5000
MAX_SEQ_LEN = 500

imdb = data.Dataset(MAX_SEQ_LEN, VOCAB_SIZE)

model = LSTM.Network(MAX_SEQ_LEN, VOCAB_SIZE)
model.summary()
model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(), metrics=['accuracy'])

# Model Training
model.fit(imdb.X_train, imdb.Y_train, batch_size=512, epochs=10, validation_split=0.2)

# Run model on test set
accr = model.evaluate(imdb.X_test, imdb.Y_test)
print('Test set\n  Loss: {:0.4f}\n  Accuracy: {:0.2f}'.format(
    accr[0], accr[1]*100))
