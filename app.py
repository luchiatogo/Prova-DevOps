from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Se você está lendo isso, meu deploy funcionou!\nFeito por: Lucas Chiacho Togo\nRA:2200537'
