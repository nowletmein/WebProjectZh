from flask import render_template, flash, redirect, jsonify
from WebApp import app, db
from WebApp.forms.subscriptionForm import SubscriptionForm
from .models import Course, Student

test_courses = [
        {'id': 1, "code" : "VEMISAB254ZF", 'name': 'Python programozas',   'students': [ 
                                                                    { "neptun" : "JJJJJJ", "name" : "John"},
                                                                    { "neptun" : "RRRRRR", "name" : "Robert"},
                                                                    { "neptun" : "MMMMMM", "name" : "Mary"}
                                                                ]},
        {'id': 2, "code" : "VEMISAB146AP",'name': 'Programozas alapjai',  'students': [ 
                                                                    { "neptun" : "KKKKKK", "name" : "Kevin"},
                                                                    { "neptun" : "WWWWWW", "name" : "William"},
                                                                    { "neptun" : "TTTTTT", "name" : "Thomas"}
                                                                ]},
        {'id': 3, "code" : "VEMISAB156GF",'name': 'Programozas I.',       'students': [
                                                                    { "neptun" : "BBBBBB", "name" : "Bob"}
                                                                ]} 
    ]
coursesDB = Course

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", name="Moodle Lite", page = "index", cnt = len(test_courses))



@app.route('/courses')
def listItems():  
    ### Write your solution here!
    courses = coursesDB.query.all()
    ###
    return render_template("courses.html", name="Moodle Lite", courses=courses, page = "courses" )
    

@app.route('/subscription', methods=["GET", "POST"])
def order():
  
  ### Write your solution here!

    form = SubscriptionForm()
    
    codeCheck = form.courseCode.data 
    searchCurse = coursesDB.query.filter_by(code=codeCheck).first()
    if form.validate_on_submit():
        if searchCurse:
            new_student = Student(
                neptun=form.neptun.data, # type: ignore
                name=form.name.data, # type: ignore
                course=searchCurse # type: ignore
            )            
            db.session.add(new_student)
            db.session.commit()
            flash("You have successfully subscribed!")
            return redirect("/courses")

        flash(f"{codeCheck} not found! Check the list!")    
            
        return redirect("/courses")
#    exists = any(course["code"] == codeCheck for course in test_courses)
#    if form.validate_on_submit():
#        if exists:
#            flash("You have successfully subscribed!")
#            for course in test_courses:
#                if course["code"] == codeCheck:
#                    course["students"].append()
#            return redirect("/index")
#        flash("nincs ilyen kúrzus kód")
    

    ###
    return render_template('subscription.html', name='Moodle Lite',page="subscription", form=form)



### Write your solution here!
@app.route('/students/<course_code>') # type: ignore
def get_students(course_code):
    course = coursesDB.query.filter_by(code=course_code).first()
    if not course:
        return jsonify({'error': 'Course not found'}), 404
    student = [{'name': student.name, 'neptun': student.neptun} for student in course.students]
    return jsonify(student)
###