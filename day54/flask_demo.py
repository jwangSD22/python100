from flask import Flask
app = Flask(__name__)

print(__name__)

if __name__== '__main__':

    app.run()

@app.route('/')
def hello_world():
    return 'hello world'
