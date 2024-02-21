from flask import Flask, request

app = Flask(__name__)


@app.get('/welcome')
def say_hello():
    """Returns a basic greeting"""
    return '<h1>welcome</h1>'


@app.get('/welcome/home')
def say_hello_home():
    """Returns a basic greeting"""
    return '<h1>welcome home</h1>'
