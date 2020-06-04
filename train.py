import LSTM
import data
import json
from keras.optimizers import RMSprop
from keras.callbacks import EarlyStopping

VOCAB_SIZE = 5000
MAX_SEQ_LEN = 500

imdb = data.Dataset(MAX_SEQ_LEN, VOCAB_SIZE)

model = LSTM.Network(MAX_SEQ_LEN, VOCAB_SIZE)
model.summary()
model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(), metrics=['accuracy'])

# Model Training
model.fit(imdb.X_train, imdb.Y_train, batch_size=512, epochs=10, validation_split=0.2, callbacks=[
    EarlyStopping(patience=2, verbose=1)
])

# Run model on test set
accr = model.evaluate(imdb.X_test, imdb.Y_test)
print('Test set\n  Loss: {:0.4f}\n  Accuracy: {:0.2f}'.format(
    accr[0], accr[1]*100))

# save weights as HDF5
model.save("model/weights.h5")
print("Saved model to disk")

# save model as JSON
model_json = model.to_json()
with open("model/model.json", "w") as file:
    file.write(model_json)

# save tokenizer as JSON
tokenizer_json = imdb.tokenizer.to_json()
with open("model/tokenizer.json", 'w', encoding='utf-8') as file:
    file.write(json.dumps(tokenizer_json, ensure_ascii=True))
