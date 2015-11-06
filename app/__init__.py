from flask import Flask  # type: ignore
from flask import render_template


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('home.html',
                           title='Home')
