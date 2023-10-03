from flask import Flask
import random
app = Flask(__name__)

print(__name__)

answer = random.sample(range(9),1)[0]

print(f'the answer is {answer}')

@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>'

@app.route('/<num>')
def greet(num):
    return f'hello!!! {num}'







if __name__== '__main__':

    app.run(debug=True)
