from flask import Flask, render_template

naukri = Flask(__name__)

IndexTemplate = 'index.html'

@naukri.route('/')
@naukri.route('/jobs')
def jobs():
    return render_template(IndexTemplate)