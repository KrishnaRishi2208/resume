import os
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import datetime
current_dir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(current_dir,"database.sqlite3")
db=SQLAlchemy()
db.init_app(app)
app.app_context().push()
deck_name=None
deck_id=None
ans=None
cards=None
counter=1
usersct=None
questions2=None
class User(db.Model):
	__tablename__='user'
	name = db.Column(db.String,nullable=False)
	institute = db.Column(db.String,nullable=False)
	info = db.Column(db.String,nullable=False)
	email = db.Column(db.String,nullable=False)
	id = db.Column(db.Integer,nullable=False,primary_key=True)

@app.route("/",methods=["Get","Post"])
def newuser():
	if request.method=="GET":
		user=User.query.filter_by(id=1).first()
		name=user.name
		desc=user.info

		return render_template("index.html",name=name,desc=desc)
@app.route("/admin",methods=["Get","Post"])
def changeuser():
	if request.method=="GET":
		user=User.query.filter_by(id=1).first()
		name=user.name
		desc=user.info
		return render_template("pass.html",name=name,desc=desc)
	if request.method=="POST":
		name = request.form.get("uname")
		desc = request.form.get("descr")
		user=User.query.filter_by(id=1).first()
		user.name=name
		user.info=desc
		db.session.add(user)
		db.session.commit()

		return redirect("/")



if __name__=="__main__":
	app.run(
		host='0.0.0.0',
		debug=False,
		port=8088)
