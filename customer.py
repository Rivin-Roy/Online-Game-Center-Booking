from public import *


customer=Blueprint('customer',__name__)

@customer.route('/customer_home')
def customer_home():
	data={}
	q="SELECT * FROM `venue` where vstatus='active'"
	res=select(q)
	data['venue']=res
	return render_template('customer_home.html',data=data)


@customer.route('/customer_edit_profile',methods=['get','post'])
def customer_edit_profile():
	data={}
	cid=session['cid']
	un=session['un']
	q="SELECT * FROM `customer` inner join login using(username) where customer_id='%s'"%(cid)
	res=select(q)
	data['res']=res

	if 'update' in request.form:
		fn=request.form['fn']
		ln=request.form['ln']
		pl=request.form['pl']
		ph=request.form['ph']
		ps=request.form['ps']
		# em=request.form['em']
		q="UPDATE `customer` SET `first_name`='%s',last_name='%s',place='%s',phone='%s' WHERE `customer_id`='%s'"%(fn,ln,pl,ph,cid)
		update(q)
		q="update login set password='%s' where username='%s'"%(ps,un)
		update(q)
		flash('updated')
		return redirect(url_for('customer.customer_edit_profile'))
	return render_template("customer_edit_profile.html",data=data)

@customer.route('/customer_send_complaints',methods=['get','post'])
def customer_send_complaints():
	data={}
	cid=session['cid']

	if 'submit' in request.form:		
		complaint=request.form['Complaint']
		q="INSERT INTO `complaint`VALUES(null,'%s','%s','pending',NOW())"%(cid,complaint)
		insert(q)

		flash("success...")

		return redirect(url_for('customer.customer_send_complaints'))

	q="SELECT * FROM `complaint` WHERE `customer_id`='%s'"%(cid)
	res=select(q)
	data['complaints']=res
	return render_template("customer_send_complaints.html",data=data)


@customer.route('/customer_view_venue')
def customer_view_venue():
	data={}
	q="SELECT * FROM `venue`"
	res=select(q)
	data['venue']=res
	return render_template("customer_view_venue.html",data=data)


@customer.route('/customer_view_timeslots')
def customer_view_timeslots():
	data={}
	cid=session['cid']
	q="SELECT * FROM `timeslot`"
	res=select(q)
	data['time']=res

	if 'action' in request.args:
		action=request.args['action']
		time_id=request.args['time_id']
		amt=request.args['amt']
	else:
		action=None

	if action=="book":
		q="select * from booking where customer_id='%s' and timeslot_id='%s'"%(cid,time_id)
		res=select(q)
		if res:
			flash("already booked this slot")
		else:
			q="insert into booking VALUES(null,'%s','%s','%s',curdate(),'pending')"%(cid,time_id,amt)
			insert(q)
			flash("booked successfully")
			return redirect(url_for('customer.customer_view_timeslots'))
	return render_template("customer_view_timeslots.html",data=data)


@customer.route('/customer_view_bookings')
def customer_view_bookings():
	data={}
	cid=session['cid']
	q="SELECT *,`timeslot`.`date` AS tdate,`booking`.`date` AS bdate FROM `booking` INNER JOIN `timeslot` USING(timeslot_id) INNER JOIN customer USING(customer_id) where customer_id='%s'"%(cid)
	res=select(q)
	data['book']=res
	return render_template("customer_view_bookings.html",data=data)

@customer.route('/customer_make_payment',methods=['get','post'])
def customer_make_payment():
	data={}
	id=request.args['id']
	amt=request.args['amt']
	data['amt']=amt


	if 'pay' in request.form:
		q="INSERT INTO `payment` VALUES(null,'%s','%s',curdate())"%(id,amt)
		insert(q)
		q="update booking set status='paid' where booking_id='%s'"%(id)
		update(q)
		flash('success...')
		return redirect(url_for('customer.customer_view_bookings'))
	return render_template("customer_make_payment.html",data=data)




@customer.route('/customer_select_date',methods=['get','post'])
def customer_select_date():
	data={}
	cid=session['cid']
	id=request.args['id']
	amt=request.args['amt']
	q="select * from timeslot where venue_id='%s'"%(id)
	res=select(q)
	data['dt']=res

	if 'add' in request.form:
		date=request.form['date']
		q="select * from booking where timeslot_id='%s'"%(date)
		res=select(q)
		if res:
			flash("This timeslot is already booked")
		else:
			q="insert into booking VALUES(null,'%s','%s','%s',curdate(),'pending')"%(cid,date,amt)
			insert(q)
			flash("booked successfully")
			return redirect(url_for('customer.customer_home'))
	return render_template("customer_select_date.html",data=data)