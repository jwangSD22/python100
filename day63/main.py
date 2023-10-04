from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'

db=SQLAlchemy()
db.init_app(app)

class Book(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(250),nullable=False,unique=True)
    author=db.Column(db.String(250),nullable=False,)
    rating=db.Column(db.Float,nullable=False)

with app.app_context():
    db.create_all()




@app.route('/')
def home():
    books = Book.query.all()



    return render_template('index.html',books=books)


@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == "POST":
        try:
            title = request.form['title']
            author = request.form['author']
            rating =request.form['rating']


            new_book = Book(title=title,author=author,rating=rating)
            db.session.add(new_book)
            db.session.commit()
            

            return redirect(url_for('home'))
        except:
            return render_template('add.html',error='INVALID INFORMATION')

    return render_template('add.html')

@app.route('/edit/<id>',methods=['GET','POST'])
def edit_rating(id):

    with app.app_context():
        book_to_update= db.session.execute(db.select(Book).where(Book.id==id)).scalar()
    if request.method== "POST":
        try:
            with app.app_context():
                book_to_update= db.session.execute(db.select(Book).where(Book.id==id)).scalar()
                book_to_update.rating = request.form['new_rating']
                db.session.commit()
            return redirect(url_for('home'))

        except:
            print('error')
            return render_template('edit_rating.html',book=book_to_update,error='Invalid Rating')

    return render_template('edit_rating.html',book=book_to_update)

if __name__ == "__main__":
    app.run(debug=True)

