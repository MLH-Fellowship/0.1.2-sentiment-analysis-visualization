from bentoml import api, env, BentoService, artifacts
from bentoml.artifact import KerasModelArtifact, PickleArtifact
from bentoml.handlers import JsonHandler
from tensorflow.keras.preprocessing import sequence, text
import data
import json

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

@artifacts([
    KerasModelArtifact('model'),
    PickleArtifact('tokenizer')
])
class SentimentClassifierService(BentoService):

    def word_to_index(self, word):
        if word in self.artifacts.tokenizer and self.artifacts.tokenizer[word] <= 5000:
            return self.artifacts.tokenizer[word]
        else:
            return self.artifacts.tokenizer["<OOV>"]

    def preprocessing(self, text_str):
        proc = text.text_to_word_sequence(data.preprocess(text_str))
        tokens = list(map(self.word_to_index, proc))
        return tokens

    @api(JsonHandler)
    def predict(self, parsed_json):
        # single pred
        input_data = [self.preprocessing(parsed_json['text'])]
        input_data = sequence.pad_sequences(input_data, maxlen=100, padding="post")
        return self.artifacts.model.predict(input_data, verbose=1)
