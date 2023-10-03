from flask import Flask
import random
app = Flask(__name__)

print(__name__)

answer = random.sample(range(9),1)[0]





@app.route('/')
def hello_world():
    return f'<h1>Guess a number between 0 and 9</h1>'\
    f'<div>the answer is {answer}</div>'


@app.route('/<int:value>')
def check_val(value):
    if value==answer:
        return f'<div>'\
    f'<h1>{value} and it is the right answer!</h1>'\
    f'</div>'
    elif value<answer:
        return f'<div>'\
        f'<h1>{value} and it is lower than the right answer!</h1>'\
    f'</div>'
    else:
        return f'<div>'\
        f'<h1>{value} and it is higher than the right answer!</h1>'\
    f'</div>'







if __name__== '__main__':

    app.run(debug=True)
