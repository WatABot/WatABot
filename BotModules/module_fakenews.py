import pandas as pd
import os
import re
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Embedding, GRU, LSTM, RNN, SpatialDropout1D
from keras.models import load_model
import nltk



model = load_model('BotModules/keras_model/model_keras.h5')

model.summary()

max_features = 4500
tokenizer = Tokenizer(num_words = max_features, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower = True, split = ' ')
# news_info = dict()
def run(inp):
  text = []
  text.append(inp)
  tokenizer.fit_on_texts(texts = text)
  test_text = tokenizer.texts_to_sequences(texts = text)
  test_text = pad_sequences(sequences = test_text, maxlen = max_features, padding = 'pre')

  result = model.predict(test_text)
  #print(result)
  return result

if __name__ == "__main__":
  run()
