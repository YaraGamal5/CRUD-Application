from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2


app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:55yara##@localhost/yaracrud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#Creating model table for CRUD database
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Title = db.Column(db.String(100))
    Department = db.Column(db.String(100))
    YearsOfExperience = db.Column(db.String(100))
    Salary = db.Column(db.Integer)


    def __init__(self, title, department, yearsOfExperience, salary):

        self.Title = title
        self.Department = department
        self.YearsOfExperience = yearsOfExperience
        self.Salary = salary



#index route 
#query on all our employee data
@app.route('/')
def Index():
    my_data = Employee.query.all()
    print(my_data)

    return render_template("index.html", employees= my_data)


#inserting data
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':
        x =10000
        title = request.form['Title']
        department = request.form['Department']
        yearsOfExperience = request.form['YearsOfExperience']
        # salary = request.form['Salary']
        # if int(salary) == 0
        #  print("10000")
        #  else 
        if yearsOfExperience =='0':
          salary = x 

        else:
         salary = int(yearsOfExperience) * 13000


        print(title)
        print(department)
        print(yearsOfExperience)
        print(salary)
        my_data = Employee(title, department, yearsOfExperience, salary)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

        return redirect(url_for('Index'))


# update data
@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
    
        delete(request.form.get('id'))
        my_data = Employee(request.form['title'], request.form['Department'], request.form['YearsOfExperience'], request.form['Salary']) 
        db.session.add(my_data)
        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for('Index'))




# deleting employees
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Employee.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('Index'))






if __name__ == "__main__":
    app.run(debug=True)


