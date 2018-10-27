from flask import Flask, render_template

app = Flask(__name__)

IndexTemplate = 'index.html'

@app.route('/')
@app.route('/jobs')
def jogibs():
    return render_template('index.html')