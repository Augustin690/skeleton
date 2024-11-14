#!/usr/bin/python3

from model import Model
from flask import *
from forms import *
from sqlite3 import IntegrityError
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


################################################################
####              HANDLING OF PERSONS                       ####
################################################################


@app.route('/person/', methods=['GET', 'POST'])
def showPersons():
    with Model() as model:
        form = PersonForm(request.form)
        if request.method == 'POST' and form.validate():
            model.createPerson(form.lastname.data, form.firstname.data,
                               form.address.data, form.phone.data)

        pers = model.listPersons()
        keys = [
            '', 'Last name', 'First name', 'Address', 'Phone', '#Curriculums',
            'Details', 'Delete'
        ]
        return render_template(
            'listing.html',
            to_list=[(pers, keys, "Persons")],
            title='Persons',
            forms=[form])


@app.route('/person/del/<id>/', methods=['POST'])
def delPerson(id=None):
    with Model() as model:
        model.deletePerson(id)
        return redirect(url_for('showPersons'))


@app.route('/person/<id>/', methods=['GET', 'POST'])
def showPerson(id=None):
    with Model() as model:
        exams = model.listExaminationsOfStudent(id)
        curri = model.listCurriculumsOfStudent(id)
        keys_exams = [
            '', 'Date', 'Curriculum', 'Course', 'Examination', 'Grade'
        ]
        keys_curri = ['Curriculum Name', 'Grade']
        return render_template(
            'listing.html',
            to_list=[
                (curri, keys_curri, "Grade overview of student \"" + model.getNameOfPerson(id) + "\""),
                (exams, keys_exams,
                 "Detailed grades of student \"" + model.getNameOfPerson(id) + "\"")
            ],
            title='Person ' + model.getNameOfPerson(id))


################################################################
####              HANDLING OF CURRICULUMS                   ####
################################################################


@app.route('/curriculum/', methods=['GET', 'POST'])
def showCurriculums():
    with Model() as model:
        form = CurriculumForm(request.form)
        form.setNames()
        if request.method == 'POST' and form.validate():
            model.createCurriculum(form.name.data, form.secretary.data,
                                   form.director.data)
        pers = model.listCurriculums()
        keys = [
            '', 'Name', 'Director last name', 'D. first name',
            'Secretary last name',
            'S. first name', 'Details', 'Delete'
        ]
        return render_template(
            'listing.html',
            to_list=[(pers, keys, "Curriculums")],
            title='Curriculums',
            forms=[form])


@app.route('/curriculum/del/<id>/', methods=['POST'])
def delCurriculum(id=None):
    with Model() as model:
        model.deleteCurriculum(id)
        return redirect(url_for('showCurriculums'))


@app.route('/curriculum/<id>/', methods=['GET', 'POST'])
def showCurriculum(id=None):
    with Model() as model:
        addStudentForm = SelectStudentForm(request.form)
        addStudentForm.setNames()
        addCourseForm = SelectCourseForm(request.form)
        addCourseForm.setNames()
        if request.method == 'POST':
            if addStudentForm.validate():
                try:
                    model.registerPersonToCurriculum(id,
                                                     addStudentForm.student.data)
                except IntegrityError:
                    addStudentForm.errors['student'] = ([
                        "This student is already registered to the curriculum!"
                    ])
            else:
                if addCourseForm.validate():
                    try:
                        model.registerCourseToCurriculum(addCourseForm.course.data,
                                                         id, addCourseForm.coef.data)
                    except IntegrityError:
                        addCourseForm.errors['course'] = ([
                            "This course is already added to the curriculum!"
                        ])
                    addStudentForm = SelectStudentForm(request.form)
                    addStudentForm.setNames()
        avg = model.averageGradesOfStudentsInCurriculum(id)
        cou = model.listCoursesOfCurriculum(id)
        keys_avg = ['Last name', 'First name', 'totalGrade']
        keys_cou = [
            '', 'Name', 'Teacher last name', 'Teacher first name', 'ECTS',
            'Delete'
        ]
        return render_template(
            'listing.html',
            to_list=[
                (avg, keys_avg, "Averaged grades of curriculum \"" +
                 model.getNameOfCurriculum(id) + "\""),
                (cou, keys_cou,
                 "Courses of curriculum \"" + model.getNameOfCurriculum(id) +
                 "\""),
            ],
            title='Curriculum ' + model.getNameOfCurriculum(id),
            forms=[addStudentForm, addCourseForm])


@app.route('/curriculum/<idCurr>/del/<idCou>/', methods=['POST'])
def delCourseFromCurriculum(idCurr=None, idCou=None):
    with Model() as model:
        model.deleteCourseFromCurriculum(idCou, idCurr)
        return redirect(url_for('showCurriculum', id=idCurr))


################################################################
####              HANDLING OF COURSES                       ####
################################################################


@app.route('/course/', methods=['GET', 'POST'])
def showCourses():
    with Model() as model:
        addCourseForm = CourseForm(request.form)
        addCourseForm.setNames()
        if request.method == 'POST' and addCourseForm.validate():
            model.createCourse(addCourseForm.name.data,
                               addCourseForm.teacher.data)
        pers = model.listCourses()
        keys = [
            '', 'Name', '', 'Teacher first name', 'Teacher last name', 'Details',
            'Delete'
        ]
        return render_template(
            'listing.html',
            to_list=[(pers, keys, "Courses")],
            title='Courses',
            forms=[addCourseForm])


@app.route('/course/del/<id>/', methods=['POST'])
def delCourse(id=None):
    with Model() as model:
        model.deleteCourse(id)
        return redirect(url_for('showCourses'))


@app.route('/course/<id>/', methods=['GET', 'POST'])
def showCourse(id=None):
    with Model() as model:
        form = ExaminationForm(request.form)
        if request.method == 'POST' and form.validate():
            model.addExaminationToCourse(form.name.data, form.coef.data, id)
        exams = model.listExaminationsOfCourse(id)
        grades = model.listGradesOfCourse(id)
        curri = model.listCurriculumsOfCourse(id)
        students = model.listStudentsOfCourse(id)
        keys_grades = [
            '', 'Date', 'Curriculum', 'Student last name', 'Student first name',
            'Examination', 'Grade', 'Coef'
        ]
        keys_exams = ['', 'Date', 'Name', 'Coef', 'Details']
        keys_curri = ['', 'Curriculum', 'ECTS']
        keys_students = ['', 'Last name', 'First name']
        return render_template(
            'listing.html',
            to_list=[(curri, keys_curri,
                      "Curriculums of course \"" + model.getNameOfCourse(id) +
                      "\""),
                     (exams, keys_exams,
                      "List of exams for course \"" + model.getNameOfCourse(id)
                      + "\""),
                     (grades, keys_grades,
                      "Grades of course \"" + model.getNameOfCourse(id) + "\""),
                     (students, keys_students,
                      "Students of course \"" + model.getNameOfCourse(id) + "\"")],
            forms=[form])


@app.route('/course/<idCourse>/<idExamination>/', methods=['GET', 'POST'])
def showExamination(idCourse=None, idExamination=None):
    with Model() as model:
        form = GradesForm(request.form)
        form.setNames(idCourse)
        if request.method == 'POST' and form.validate():
            try:
                model.addGrade(idExamination, form.student.data,
                               str(form.grade.data))
            except IntegrityError:
                form.errors['student'] = ([
                    "This student already has a grade!"
                ])

        grades = model.listGradesOfExamination(idExamination)
        keys_grades = ['Grade', 'First name', 'Last name']
        return render_template(
            'listing.html',
            to_list=[(grades, keys_grades,
                      "Grades for \"" + model.getNameOfExamination(idExamination) + "\"")],
            forms=[form])


################################################################
####              HANDLING OF ROOOMS                        ####
################################################################


@app.route('/room/', methods=['GET', 'POST'])
def showRooms():
    with Model() as model:
        addRoomForm = RoomForm(request.form)
        if request.method == 'POST' and addRoomForm.validate():
            model.createRoom(addRoomForm.name.data, addRoomForm.capacity.data)
        pers = model.listRooms()
        keys = ['', 'Name', 'Capacity', 'Details', 'Delete']
        return render_template(
            'listing.html',
            to_list=[(pers, keys, "Rooms")],
            forms=[addRoomForm])


@app.route('/room/del/<id>/', methods=['POST'])
def delRoom(id=None):
    with Model() as model:
        model.deleteRoom(id)
        return redirect(url_for('showRooms'))


@app.route('/room/<id>/', methods=['GET', 'POST'])
def showRoom(id=None):
    with Model() as model:
        form = OccupyForm(request.form)
        form.setNames()
        if request.method == 'POST' and form.validate():
            model.occupyRoom(id, form.course.data, form.start.data.strip(),
                             form.end.data.strip())
        exams = model.listCoursesInRoom(id)
        keys = ['Start', 'End', 'Course name']
        return render_template(
            'listing.html',
            to_list=[(exams, keys,
                      "Reservations for room \"" + model.getNameOfRoom(id) +
                      "\"")],
            forms=[form])


if __name__ == '__main__':
    app.run(debug=True)
