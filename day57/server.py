from flask import Flask, render_template
import random
from datetime import datetime as dt
import requests
import json


app = Flask(__name__)

@app.route('/')
def index():
    random_number = random.randint(1,10)
    current_year = dt.now().year
    return render_template('index.html',num=random_number,year=current_year)

@app.route('/guess/<name>')
def guess(name):
    def getage(name):

        age = requests.get(f'https://api.agify.io/?name={name}')

        dict = age.json()

        return dict['age']


    def getgender(name):

        gender = requests.get(f'https://api.genderize.io?name={name}')
        dict = gender.json()

        return dict['gender']

    age = getage(name)
    gender = getgender(name)


    return render_template('guess.html',name=name,age=age,gender=gender)

@app.route('/blog')
def blog():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    posts = response.json()
    return render_template('blog.html',posts=posts)



if __name__ == '__main__':
    app.run(debug=True)






