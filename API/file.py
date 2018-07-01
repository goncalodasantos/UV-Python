from flask import Flask
app = Flask(__name__)

list_of_messages=[]

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/messages/')
def messages():
    string_to_return=""
    print("ola")
    for c in list_of_messages:
        string_to_return+=c+"<br>"
    return 'Messages:'+"<br>"+string_to_return


@app.route('/messages/<message>')
def message(message):
    list_of_messages.append(message)
    string_to_return=""
    for c in list_of_messages:
        string_to_return+=c+"<br>"
    return 'Messages:'+"<br>"+string_to_return