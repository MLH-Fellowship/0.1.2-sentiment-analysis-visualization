# sentiment analysis visualization
## pod 0.1.2
A web-app the helps to visualize a character-by-character breakdown of how sentiment analysis classifies text

## major goals
* Research and decide on a machine learning model/architecture
* Pick out 2-3 datasets we can use to train
* Build a training pipeline
* Train and implement the model
* Serve the model using BentoML as an API
* Create a web app to take in input and visualize the output

## simple deep LSTM architecture
```python
> model.summary()
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
inputs (InputLayer)          (None, 500)               0
_________________________________________________________________
embedding_1 (Embedding)      (None, 500, 64)           64000
_________________________________________________________________
lstm_1 (LSTM)                (None, 500, 64)           33024
_________________________________________________________________
dropout_1 (Dropout)          (None, 500, 64)           0
_________________________________________________________________
lstm_2 (LSTM)                (None, 64)                33024
_________________________________________________________________
FC1 (Dense)                  (None, 256)               16640
_________________________________________________________________
dropout_2 (Dropout)          (None, 256)               0
_________________________________________________________________
out_layer (Dense)            (None, 1)                 257
_________________________________________________________________
activation_1 (Activation)    (None, 1)                 0
=================================================================
Total params: 146,945
Trainable params: 146,945
Non-trainable params: 0
_________________________________________________________________
```
## Installation for local environment
* Install BentoML
* Install Docker 
  * if using Windows, will need Docker Desktop Edge available through Windows inside program. Must install a WSL distribution of Linux. We used "Remote WSL extension" in VSCode. 
