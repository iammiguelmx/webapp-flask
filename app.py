# ==============================================================
# Author: Miguel Camacho
# Email: miguel.cam.mx@gmail.com
# Twitter: @elmiguelmx
#
# ==============================================================

# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)