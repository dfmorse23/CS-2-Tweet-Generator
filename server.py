from flask import Flask
the_app = Flask(__name__)

@the_app.route('/')
def hello_word():
    print("hellow world")
