from flask import render_template
from app import app
from app.forms import PartForm,QueryForm,UpdateForm,DeleteIdform,DeleteLocationform
from app import db
from flask import request
from app.models import Partnum
import flask



@app.route('/')
@app.route('/index')
def index():
    form2 = UpdateForm()
    form1 = QueryForm()
    form = PartForm()
    return render_template('index.html', title='Home',form=form)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = PartForm()

    if form.validate_on_submit():
        partnumber = request.form['partnumber']
        location = request.form['location']
        quantity = request.form['quantity']
        description = request.form['description']
        newPart = Partnum(partnumber=partnumber, location=location, quantity=quantity, description=description)
        db.session.add(newPart)
        db.session.commit()        
        return render_template('index.html', form=form)

@app.route('/query', methods=['GET','POST'])
def query():
   # selectedpart=[Partnum(partnumber='wr30x10093', location='v',quantity=5,description='none'),Partnum(partnumber='rt30x10093', location='va',quantity=56,description='norne')]
    selectedpart=[]
    form1 = QueryForm()
    if form1.validate_on_submit():        
        partnumber = request.form['partnumber'] 
        location = request.form['location']
        if partnumber:
            selectedpart = Partnum.query.filter_by(partnumber=partnumber).all()
        elif location:
            selectedpart = Partnum.query.filter_by(location=location).all()

        return render_template('query.html', form1=form1,selectedpart=selectedpart,location=location)
    return render_template('query.html', form1=form1, selectedpart=selectedpart)    


@app.route('/update', methods=['GET','POST'])
def update():
    form2=UpdateForm()
    
    if flask.request.method == 'GET':
        data=request.args.get('data')
        numdata=int(data)
        parsel = Partnum.query.get(numdata)

    if form2.validate_on_submit():
        idd = request.form['idd']
        partnumber = request.form['partnumber']
        location = request.form['location']
        quantity = request.form['quantity']
        description = request.form['description']
        numdata=int(idd)
        parsel = Partnum.query.get(numdata)
        parsel.partnumber = partnumber
        parsel.location = location
        parsel.quantity = quantity
        parsel.description = description
        db.session.commit()
    return render_template('update.html',form2=form2, parsel=parsel)

@app.route('/delete', methods=['GET','POST'])
def delete():
    dpart=[]
    form3=DeleteIdform()
    form4=DeleteLocationform()
    if form3.validate_on_submit():        
        idd = request.form['idd']
        dpart = Partnum.query.get(idd)

        db.session.delete(dpart)
        db.session.commit()

        return render_template('delete.html', form3=form3,form4=form4)
    if form4.validate_on_submit():
        location = request.form['location']

        Partnum.query.filter_by(location=location).delete()
        db.session.commit()







        return render_template('delete.html', form3=form3, form4=form4)
    return render_template('delete.html', form3=form3,form4=form4, dpart=dpart)  




    


    






    

