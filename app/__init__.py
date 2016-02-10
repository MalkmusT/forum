from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
import pygal
from pygal.style import DarkSolarizedStyle

app = Flask( __name__ )

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()

@app.route("/")
def home_view () :
    return render_template( "base.html" )

@app.route( "/bootstrap" )
def bootstrap () :
    return render_template( "bootstrap.html" ) 

@app.route( "/project", methods = [ "GET", "POST" ] )
def view () :
    if request.method == "GET" :
        return render_template("project.html", users=User.query.all() )
    elif request.method == "POST" :
        db.session.add(User( username=request.form.get("name") ) )
        db.session.commit()
        return render_template("project.html", users=User.query.all() )
