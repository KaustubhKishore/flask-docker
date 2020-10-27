from flask import Flask, request, render_template,redirect

import os
import re

from flask_sqlalchemy import SQLAlchemy

cmd = "head -1 /proc/self/cgroup|cut -d/ -f3"
cmd_out = os.popen(cmd).read()

app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "db/bookdatabase.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)


var = 0
pagehits = 0
visitors = list()

@app.route('/', methods=["GET", "POST"])
def index():
    global var, pagehits, visitors
    # if(request.remote_addr not in visitors):
        # var += 1
        # visitors.append(request.remote_addr)
    # else:
        # pagehits += 1
    var += 1
    pagehits +=1

    books = None
    if request.form:
        try:
            book = Book(title=request.form.get("title"))
            db.session.add(book)
            db.session.commit()
        except Exception as e:
            print("Failed to add book")
            print(e)
    books = Book.query.all()


    return render_template('index.html',value = var, cont = cmd_out, allbooks = books, pagec =pagehits)

@app.route("/update", methods=["POST"])
def update():
    try:
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        book = Book.query.filter_by(title=oldtitle).first()
        book.title = newtitle
        db.session.commit()
    except Exception as e:
        print("Couldn't update book title")
        print(e)
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
    