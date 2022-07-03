from public import *


admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
	return render_template('admin_home.html')

@admin.route('/admin_manage_venue',methods=['get','post'])
def admin_manage_venue():
	data={}

	if 'action' in request.args:
		action=request.args['action']
		ids=request.args['ids']
	else:
		action=None

	if action=='inactive':
		q="update venue set vstatus='inactive' where venue_id='%s'"%(ids)
		update(q)
		flash("activated")
		return redirect(url_for('admin.admin_manage_venue'))
	if action=='active':
		q="update venue set vstatus='active' where venue_id='%s'"%(ids)
		update(q)
		flash("Inactivated")
		return redirect(url_for('admin.admin_manage_venue'))

	if action=='update':
		q="SELECT * FROM `venue` WHERE `venue_id`='%s'"%(ids)
		res=select(q)
		data['res']=res

	if 'update' in request.form:
		venue=request.form['venue']
		place=request.form['pl']
		a=request.form['a']
		
		details=request.form['det']
		q="UPDATE `venue` SET `venue`='%s',place='%s',amount='%s',details='%s' WHERE `venue_id`='%s'"%(venue,place,a,details,ids)
		update(q)
		flash('updated')
		return redirect(url_for('admin.admin_manage_venue'))

	if 'submit' in request.form:
		venue=request.form['venue']
		place=request.form['pl']
	
		a=request.form['a']
		details=request.form['det']
		q="INSERT INTO `venue` VALUES(null,'%s','%s','%s','%s','active')"%(venue,place,a,details)
		insert(q)
		flash('venue added')
		return redirect(url_for('admin.admin_manage_venue'))

	q="SELECT * FROM `venue`"
	res=select(q)
	data['venue']=res
	return render_template('admin_manage_venue.html',data=data)


@admin.route('/admin_manage_time_slot',methods=['get','post'])
def admin_manage_time_slot():
	data={}
	id=request.args['id']
	data['id']=id

	if 'action' in request.args:
		action=request.args['action']
		ids=request.args['ids']
	else:
		action=None

	if action=='inactive':
		q="update timeslot set mstatus='inactive' where timeslot_id='%s'"%(ids)
		update(q)
		flash("activated")
		return redirect(url_for('admin.admin_manage_time_slot'))
	if action=='active':
		q="update timeslot set mstatus='active' where timeslot_id='%s'"%(ids)
		update(q)
		flash("Inactivated")
		return redirect(url_for('admin.admin_manage_time_slot'))

	if action=='update':
		q="SELECT * FROM `timeslot` WHERE `timeslot_id`='%s'"%(ids)
		res=select(q)
		data['res']=res

	if 'update' in request.form:
		time=request.form['slot']
		fromt=request.form['ft']
		tot=request.form['tt']
		q="UPDATE `timeslot` SET `timeslot`='%s',fromtime='%s',totime='%s',amount='%s' WHERE `timeslot_id`='%s'"%(time,fromt,tot,amt,ids)
		update(q)
		flash('updated')
		return redirect(url_for('admin.admin_manage_time_slot',id=id))

	if 'submit' in request.form:
		time=request.form['slot']
		fromt=request.form['ft']
		tot=request.form['tt']
		amt=request.form['amt']
		q="select * from timeslot where time='%s' "
		q="INSERT INTO `timeslot` VALUES(null,'%s','%s','%s','%s','%s','active')"%(id,time,fromt,tot,amt)
		insert(q)
		flash('timeslot added')
		return redirect(url_for('admin.admin_manage_time_slot',id=id))

	q="SELECT * FROM `timeslot`"
	res=select(q)
	data['time']=res
	return render_template("admin_manage_time_slot.html",data=data)


@admin.route('/admin_view_complaint_reply',methods=['get','post'])
def admin_view_complaint_reply():
	data={}
	q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS `name` FROM `complaint` INNER JOIN `customer` USING(`customer_id`)"
	res=select(q)
	data['complaints']=res

	j=0
	for i in range(1,len(res)+1):
		print('submit'+str(i))
		if 'submit'+str(i) in request.form:
			reply=request.form['reply'+str(i)]
			print(reply)
			print(j)
			print(res[j]['complaint_id'])
			q="update complaint set reply='%s' where complaint_id='%s'" %(reply,res[j]['complaint_id'])
			print(q)
			update(q)
			flash("success")
			return redirect(url_for('admin.admin_view_complaint_reply')) 	
		j=j+1
	return render_template("admin_view_complaint_reply.html",data=data)


@admin.route('/admin_view_bookings')
def admin_view_bookings():
	data={}
	q="SELECT * FROM `booking` INNER JOIN `timeslot` USING(timeslot_id) INNER JOIN `customer` USING(customer_id)"
	res=select(q)
	data['book']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=='accept':
		q="update booking set status='Accepted' where booking_id='%s'"%(id)
		update(q)
		flash('accepted')
		return redirect(url_for('admin.admin_view_bookings'))

	if action=='reject':
		q="update booking set status='Rejected' where booking_id='%s'"%(id)
		update(q)
		flash('rejected')
		return redirect(url_for('admin.admin_view_bookings'))
	return render_template("admin_view_bookings.html",data=data)

@admin.route('/admin_view_payments')	
def admin_view_payments():
	data={}
	id=request.args['id']
	q="SELECT * FROM `payment` WHERE booking_id='%s'"%(id)
	res=select(q)
	data['pay']=res
	return render_template("admin_view_payments.html",data=data)



@admin.route('/admin_add_staff',methods=['get','post'])
def admin_add_staff():
	data={}
	q="SELECT  * FROM `staff`"
	data['staff']=select(q)


	if 'action' in request.args:
		action=request.args['action']
		sid=request.args['sid']
	else:
		action=None

	if action=='update':
		q="select * from staff where username='%s'"%(sid)
		data['updatess']=select(q)

	if action=='inactive':
		q="update staff set fstatus='inactive' where username='%s'"%(sid)
		update(q)
		q="update login set user_type='staffs' where username='%s'"%(sid)
		update(q)
		flash("Inactivated")
		return redirect(url_for('admin.admin_add_staff'))
	if action=='active':
		q="update staff set fstatus='active' where username='%s'"%(sid)
		update(q)
		q="update login set user_type='staff' where username='%s'"%(sid)
		update(q)
		flash("Activated")
		return redirect(url_for('admin.admin_add_staff'))

	if 'submits' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		hname=request.form['hname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		

		# q="update `login` set `username'=%s' where "%(email,pwd)
		# insert(q)
		q="update `staff` set `username`='%s',`first_name`='%s',`last_name`='%s',`house_name`='%s',`place`='%s',`phone`='%s',`email`='%s' where username='%s'"%(email,fname,lname,hname,place,phone,email,sid)
		update(q)
		flash('successfully updated')
		return redirect(url_for('admin.admin_add_staff'))

	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		hname=request.form['hname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		pwd=request.form['pwd']

		q="INSERT INTO `login` VALUES('%s','%s','staff')"%(email,pwd)
		insert(q)
		q="INSERT INTO `staff` VALUES(null,'%s','%s','%s','%s','%s','%s','%s','active')"%(email,fname,lname,hname,place,phone,email)

		insert(q)
		flash('success...')
		return redirect(url_for('admin.admin_add_staff'))
	return render_template('admin_add_staff.html',data=data)