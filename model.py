#!/usr/bin/python3

import sys
import sqlite3


class Model:

    def openDB(self, db):
        self.connection = sqlite3.connect(db)
        self.connection.execute("PRAGMA foreign_keys = 1")
        self.connection.text_factory = str
        self.cursor = self.connection.cursor()
        
    
    def __init__(self):
        self.openDB('univ.db')
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if (self.connection):
            self.connection.close()

##############################################
######        Queries for tab  ROOMS    ######
##############################################

    # Q1. Create a new room from the room name and capacity
    def createRoom(self, name, capacity):
        self.cursor.execute("""
        INSERT INTO rooms (name,capacity) VALUES (?,?)
        """, (name, capacity))
        self.connection.commit()

    # Q2. Delete a room given by its ID (beware of foreign key constraints!)
    def deleteRoom(self, idRoom):
        self.cursor.execute("""
        TODO2
        """, (idRoom,))
        self.connection.commit()

    # Q3. Return a list of all rooms in the format (id, name, capacity)
    def listRooms(self):
        self.cursor.execute(""" 
        TODO3
        """)
        return self.cursor.fetchall()

##############################################
######     Queries for tab  COURSES     ######
##############################################

    # Q4. Create a course from the course name and the ID of the
    # teacher of the course
    def createCourse(self, name, idProfessor):
        self.cursor.execute("""
        TODO4
        """, (name, idProfessor))
        self.connection.commit()

    # Q5. Delete a course given by its ID (beware of foreign key constraints!)
    def deleteCourse(self, idCourse):
        self.cursor.execute("""
        TODO5
        """, (idCourse,))
        self.connection.commit()

    # Q6. Return a list of all courses in the format:
    # (course id, course name, teacher id, teacher lastname, teacher firstname)
    def listCourses(self):
        self.cursor.execute(""" 
        TODO6
        """)
        return self.cursor.fetchall()

##############################################
######     Queries for tab  CURRICULUMS ######
##############################################

    # Q7. Create a new curriculum from the curriculum name, secretary ID, and
    # director ID
    def createCurriculum(self, name, secretary, director):
        self.cursor.execute("""
        TODO7
        """, (name, secretary, director))
        self.connection.commit()

    # Q8. Delete a curriculum given by its ID (beware of foreign key constraints!)
    def deleteCurriculum(self, idCurriculum):
        self.cursor.execute("""
        TODO8
        """, (idCurriculum,))
        self.connection.commit()

    # Q9. Return a list of all curriculums in the format:
    # (id,name of curriculum,director lastname, director firstname,
    # secretary lastname, secretary firstname)
    def listCurriculums(self):
        self.cursor.execute(""" 
        TODO9
        """)
        return self.cursor.fetchall()

##############################################
######      Queries for tab  PERSONS    ######
##############################################

    # Q10. Create a new person from the first name, last name, address, and phone
    # number
    def createPerson(self, lastname, firstname, address, phone):
        self.cursor.execute("""
        TODO10
        """, (lastname, firstname, address, phone))
        self.connection.commit()

    # Q11. Delete a person given by its ID (beware of foreign key constraints)
    def deletePerson(self, idPerson):
        self.cursor.execute("""
        TODO11
        """, (idPerson,))
        self.connection.commit()

    # Q12. Return a list of all persons, indicating for each of them:
    # (lastname, firstname, address, phone, number of registered curriculums)
    def listPersons(self):
        self.cursor.execute(""" 
        TODO12
        """)
        return self.cursor.fetchall()


##############################################
######   Queries for tab  ROOM/<ID>     ######
##############################################

    # Q13. Get the name of a Room from its id
    def getNameOfRoom(self, id):
        self.cursor.execute(""" 
        TODO13
        """, (id,))
        # suppose that there is a solution
        return self.cursor.fetchall()[0][0]

    # Q14. Reserve a time range (since, until) for idCourse in room idRoom.
    # (You do not need to verify that there are no two conflicting
    # reservations.)
    def occupyRoom(self, idRoom, idCourse, since, until):
        self.cursor.execute("""
        TODO14
        """, (idRoom, idCourse, since, until))
        self.connection.commit()

    # Q15. Return the reservations of a given room in the form
    # (start,end,course name) ordered by decreasing start date
    def listCoursesInRoom(self, idRoom):
        self.cursor.execute("""
        TODO15
        """, (idRoom,))
        return self.cursor.fetchall()

##############################################
######   Queries for tab  COURSE/<ID>   ######
##############################################

    # Q16. Get the name of the course given by its id
    def getNameOfCourse(self, id):
        self.cursor.execute(""" 
        TODO16
        """, (id,))
        # suppose that there is a solution
        return self.cursor.fetchall()[0][0]

    # Q17. Return a list of the curriculums in which a course is registered
    # in the format (id, name, ECTS)
    def listCurriculumsOfCourse(self, idCourse):
        self.cursor.execute("""
        TODO17
        """, (idCourse,))
        return self.cursor.fetchall()

    # Q18. Return a list of (id, date, name, coefficient) for an examination
    def listExaminationsOfCourse(self, idCourse):
        self.cursor.execute("""
        TODO18
        """, (idCourse,))
        return self.cursor.fetchall()

    # Q19. Return a list of the students registered in a curriculum that
    # contains this course, in the format
    # (lastname,firstname,student id)
    def listStudentsOfCourse(self, idCourse):
        self.cursor.execute("""
        TODO19
        """, (idCourse,))
        return self.cursor.fetchall()

    # Q20. Given the id of a course, return a list (exam id, exam date, curriculum name,
    # student lastname, student firstname, exam name, grade) of all known
    # student grades for
    # the course, sorted by exam date
    def listGradesOfCourse(self, idCourse):
        self.cursor.execute("""
        TODO20
        """, (idCourse,))
        return self.cursor.fetchall()

    # Q21. Add an examination (having a name and coefficient) to a course
    def addExaminationToCourse(self, name, coef, idCourse):
        self.cursor.execute(""" 
        TODO21
        """, (name, coef, idCourse))
        self.connection.commit()

    # Q22. Add a grade to a student for an examination
    def addGrade(self, idExamination, idStudent, grade):
        self.cursor.execute(""" 
        TODO22
        """, (idExamination, idStudent, grade))
        self.connection.commit()

##############################################
######       Queries for tab            ######
######      COURSE/<ID1>/<ID2           ######
###### corresponding to examinations    ######
##############################################

   # Q23. Return a list
   # (grade, lastname, firstname)
   # of all grades for an examination
    def listGradesOfExamination(self, idExamination):
        self.cursor.execute("""
        TODO23
        """, (idExamination,))
        return self.cursor.fetchall()

    # Q24. Get the complete name of the examination given by its id. The
    # complete name of an examination with name "exam" of a course "BDD"
    # is "BDD - exam". You should therefore prepend the name of the
    # course
    def getNameOfExamination(self, id):
        self.cursor.execute(""" 
        TODO24
        """, (id,))
        # suppose that there is a solution
        return self.cursor.fetchall()[0][0]

##############################################
###### Queries for tab  CURRICULUM/<ID> ######
##############################################

    # Q25. Get the name of the curriculum given by its id
    def getNameOfCurriculum(self, id):
        self.cursor.execute(""" 
        TODO25
        """, (id,))
        # suppose that there is a solution
        return self.cursor.fetchall()[0][0]

    # Q26. List the courses that are part of a curriculum (given by its ID), in
    # the format (course ID, course name, course teacher lastname and firstname,
    # ECTS)
    def listCoursesOfCurriculum(self, idCurriculum):
        self.cursor.execute("""
        TODO26
        """, (idCurriculum,))
        return self.cursor.fetchall()

    # Q27. Register a person (given by its ID) to a curriculum (given by its ID)
    def registerPersonToCurriculum(self, idPerson, idCurriculum):
        self.cursor.execute("""
        TODO27
        """, (idPerson, idCurriculum))
        self.connection.commit()

    # Q28. Add a course (given by its ID) to a curriculum (given by its ID)
    def registerCourseToCurriculum(self, idCourse, idCurriculum, coef):
        self.cursor.execute("""
        TODO28
        """, (idCurriculum, idCourse, coef))
        self.connection.commit()

    # Q29. Unregister a course (given by its ID) to a curriculum (given by its ID)
    def deleteCourseFromCurriculum(self, idCourse, idCurriculum):
        self.cursor.execute("""
        TODO29
        """, (idCurriculum, idCourse))
        self.connection.commit()

    # !! HARD !!
    # Q30. This function should return the students registered
    # in a given curriculum and their average. The result is a list of:
    # (lastname, firstname, averageGrade). The average of a student for a
    # curriculum is the average of their grade in every course of the curriculum,
    # each course being weighted by its ECTS value in the curriculum. The
    # average of a student for a course is the average of their grade in every
    # examination of the course, weighted by the coefficient of the examination.
    # Students who do not have a registered grade for a examination should be
    # counted as having 0 by default.
    def averageGradesOfStudentsInCurriculum(self, idCurriculum):
        self.cursor.execute("""
        TODO30
        """, (idCurriculum,))
        return self.cursor.fetchall()


##############################################
######   Queries for tab  PERSON/<ID>   ######
##############################################

    # Q31. Get the name of the person given by its id
    def getNameOfPerson(self, id):
        self.cursor.execute(""" 
        TODO31
        """, (id,))
        # suppose that there is a solution
        return self.cursor.fetchall()[0][0]

    # Q32. Given the id of a student, return a list
    # (id, date, curriculum name, course name, exam name, grade)
    # of all exams taken by this student and their grade, sorted by decreasing
    # exam date
    def listExaminationsOfStudent(self, idStudent):
        self.cursor.execute("""
        TODO32
        """, (idStudent,))
        return self.cursor.fetchall()

    # !! HARD !!
    # Q33. List the curriculums in which a student is registered and return a
    # list (curriculum name, grade) where grade is the average grade
    def listCurriculumsOfStudent(self, idStudent):
        self.cursor.execute("""
        TODO33
        """, (idStudent,))
        return self.cursor.fetchall()

