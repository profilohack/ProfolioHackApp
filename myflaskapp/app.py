from flask import Flask, render_template, url_for
from data import Articles
from forms import RegistrationForm
import suggest

app = Flask(__name__)

Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def batman():
    suggested_amount, net_income, customer_name = suggest.suggest("Bat Man")
    suggested_amount = round(suggested_amount,2)
    net_income = round(net_income,2)
    return render_template('about.html',suggested_amount = suggested_amount, net_income = net_income, customer_name = customer_name)
"""
@app.route('/about')
def about():
    return render_template('about.html')"""

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)
    
@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


if __name__=='__main__':
    app.run(debug=True)