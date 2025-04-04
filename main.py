from flask import Flask, render_template, jsonify, request, redirect, url_for

from db import get_data

app = Flask(__name__)

#Current page tracker
page = None

@app.route('/')
def entry():
    global page
    page = 'neg'
    return redirect(url_for('neg'))

@app.route('/neg')
def neg():
    global page
    page = 'neg'
    return render_template('neg.html')

@app.route('/pos')
def pos():
    global page
    page = 'pos'
    return render_template('pos.html')


#Data requests of website
@app.route('/data')
def data():
    item = request.args.get('item', default=1, type=str)
    print("*** CALLING {}, {}***".format(item,page))
    data = get_data(item,page)
    return jsonify(data)

if __name__ == '__main__':
    app.run()
