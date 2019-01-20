from flask import Flask, render_template, url_for
from data import Articles
from forms import RegistrationForm
import suggest
import _yield
from getData import getAllFiles

app = Flask(__name__)

Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')
"""
@app.route('/about')
def chart():
    return render_template('chart.html')"""

@app.route('/about')
def batman():
    suggested_amount, net_income, customer_name = suggest.suggest("Bat Man")
    suggested_amount = round(suggested_amount,2)
    net_income = round(net_income,2)
    returns = getAllFiles()
    weights = _yield.covar(returns)
    return render_template('about.html',suggested_amount = suggested_amount, net_income = net_income, customer_name = customer_name, weights = weights)

"""
@app.route('/about')
def about():
    return render_template('about.html')"""

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)
"""
@app.route('/articles')
def articles():
    return render_template('line.html')"""


@app.route('/article/Bonds/')
def bonds():
    return render_template('bonds.html')

@app.route('/article/Mutual Funds/')
def mutual():
    return render_template('mutual.html')

@app.route('/article/Stocks/')
def stocks():
    return render_template('stocks.html')
    
@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


if __name__=='__main__':
    app.run(debug=True)