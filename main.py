from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'My name is Jakup er her endnu...'

if __name__ == '__main__':
  app.run()
