from flask import Flask
from keras.models import Sequential

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Importeret Keras.models'

if __name__ == '__main__':
  app.run()
