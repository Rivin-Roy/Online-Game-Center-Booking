from flask import *
from database import *
import uuid

public=Blueprint('public',__name__)

@public.route('/')
def home():
	data={}
	q="SELECT * FROM `venue` where vstatus='active'"
	res=select(q)
	data['venue']=res
	return render_template('home.html',data=data)

@public.route('/login',methods=['get','post'])
def login():

	if 'submit' in request.form:
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="SELECT * FROM `login` WHERE `username`='%s' AND `password`='%s'"%(uname,pwd)
		res=select(q)
		if res:
			session['uname']=res[0]['username']
			if res[0]['user_type']=='admin':
				flash("login successfully....!")
				return redirect(url_for('admin.admin_home'))
			elif res[0]['user_type']=='customer':
				q="select * from customer where username='%s'"%(session['uname'])
				res=select(q)
				print(res)
				if res:
					session['cid']=res[0]['customer_id']
					session['un']=res[0]['username']
					flash("login successfully....!")
					return redirect(url_for('customer.customer_home'))
			elif res[0]['user_type']=='staff':
				q="select * from staff where username='%s'"%(session['uname'])
				res=select(q)
				print(res)
				if res:
					session['sid']=res[0]['staff_id']
					flash("login successfully....!")
					return redirect(url_for('staff.staff_home'))
		else:
			flash("INVALID USERNAME OR PASSWORD")
	return render_template('login.html')


@public.route('/customer_register',methods=['get','post'])
def customer_register():
	if 'submit' in request.form:
		fname=request.form['fn']
		lname=request.form['ln']
		place=request.form['pl']
		phone=request.form['ph']
		email=request.form['em']
		pwd=request.form['pwd']
		q="select * from login where username='%s' and password='%s'" %(email,pwd)
		res=select(q)
		if res:
			flash("USERNAME AND PASSWORD IS ALREADY EXIST")
		else:
			q="INSERT INTO `login` VALUES('%s','%s','customer')"%(email,pwd)
			insert(q)
			q1="INSERT INTO `customer` VALUES(null,'%s','%s','%s','%s','%s','%s')"%(email,fname,lname,place,phone,email)
			insert(q1)
			flash('registered')
		return redirect(url_for('public.customer_register'))
	return render_template("customer_register.html")