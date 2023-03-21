from app import application
from flask import render_template

@application.route('/welcome')
def welcome():
    return render_template('index.html')

@application.route('/topfive')
def top_five():
    return 'My top five favorite cars: 1. Mclaren 765LT 2. Ferrari SF90 3. Lamorghini Aventador 4. BMW M8 5. Porsche 911 GT3RS'