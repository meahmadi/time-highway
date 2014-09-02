# -*- coding: utf-8 -*-

from flask import Flask, abort, render_template

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/')
def intro():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

