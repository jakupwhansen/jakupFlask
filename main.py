from flask import Flask
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
import numpy

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'alt vek...'

if __name__ == '__main__':
  app.run()
