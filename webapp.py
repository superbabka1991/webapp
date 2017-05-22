from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import statistics

app = Flask(__name__, )
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mrychlik:HNDgWkiyxUQ1vUY2@mysql.agh.edu.pl/formdata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

db = SQLAlchemy(app)

class Formdata(db.Model):
    __tablename__ = 'formdata'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    sex = db.Column(db.String(10))
    age = db.Column(db.String(15))
    edu = db.Column(db.String(10))
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)
    q6 = db.Column(db.Integer)
    q7 = db.Column(db.Integer)
    q8 = db.Column(db.Integer)
    q9 = db.Column(db.Integer)
    q10 = db.Column(db.Integer)
    #sprawdzic wielokrotna odp
    #q11 = db.Column(db.Double[])
    #^^wieloktrona odpowiedź
    #q12 = db.Column(db.Integer)
    #q13 = db.Column(db.Integer)
    #q14 = db.Column(db.Integer)
    #q15 = db.Column(db.Integer)
    #q16 = db.Column(db.Integer)
    #q17 = db.Column(db.String)


    def __init__(self, sex, age, edu, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):

        self.sex = sex
        self.age = age
        self.edu = edu
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.q10 = q10
        #self.q11 = q11
        #self.q12 = q12
        #self.q13 = q13
        #self.q14 = q14
        #self.q15 = q15
        #self.q16 = q16
        #self.q17 = q17

db.create_all()


@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route("/form")
def show_form():
    return render_template('form.html')

@app.route("/raw")
def show_raw():
    fd_list = db.session.query(Formdata).all()
    # opracowanie statystyk
    return render_template('raw.html', formdata=fd_list)

@app.route("/text")
def text():
    return render_template('text.html')

@app.route("/result")
def show_result():
    fd = db.session.query(Formdata).all()

    return render_template('result.html', formdata=fd)


@app.route("/save", methods=['POST'])
def save():
    # Get data from FORM

    sex = request.form['sex']
    age = request.form['age']
    edu = request.form['edu']
    q1 = request.form['q1']
    q2 = request.form['q2']
    q3 = request.form['q3']
    q4 = request.form['q4']
    q5 = request.form['q5']
    q6 = request.form['q6']
    q7 = request.form['q7']
    q8 = request.form['q8']
    q9 = request.form['q9']
    q10 = request.form['q10']
    #q11 = request.form['q11']
    #q12 = request.form['q12']
    #q13 = request.form['q13']
    #q14 = request.form['q14']
    #q15 = request.form['q15']
    #q16 = request.form['q16']
    #q17 = request.form['q17']

    # Save the data
    fd = Formdata( sex, age, edu, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
    db.session.add(fd)
    db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    app.debug = True
    app.run()