from flask import Flask, redirect, request, url_for, render_template
from db import get_customers_p, get_songs, create, get_songs_by_title

app = Flask(__name__)

@app.route('/')
@app.route('/about')
@app.route('/insert_form')
@app.route('/search_form')
def static_pages():
    page = request.path.strip('/')
    return render_template(f"{page or 'index'}.html")

@app.route('/customer_p')
def customer_p():
    return render_template('customer_p.html', customers=get_customer_p())

@app.route('/display')
def display():
    return render_template('display.html', songs=get_songs())

@app.route('/add', methods=['POST'])
def add():
    create(request.form['title'], request.form['artist'], request.form['genre'])
    return redirect(url_for('display'))

#search song
@app.route('/search', methods=['POST'])
def search():
    title_query = request.form.get('title', '')
    results = get_songs_by_title(title_query) if title_query else []
    return render_template('display.html', songs = results)

if __name__ == '__main__':
    app.run(debug=True)
