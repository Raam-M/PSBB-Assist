import mysql.connector
import dbconfig as db

# Function to retrieve all the students in a class
def getStudentsbyClass(idclass=""):
    cnx = mysql.connector.connect(**db.config)
    cursor = cnx.cursor()
    whereclause = ""
    if len(idclass) > 0:
        whereclause += "idclass = \"" + idclass + "\""
    if len(whereclause)>0:
      whereclause = "WHERE " + whereclause
    query_students = ("SELECT idstudent, studfname, studlname,idstudclass, idclass FROM vw_studentclass "+ whereclause)
    cursor.execute(query_students)
    listStudents = []
    for student in cursor:
      listStudents.append(student)
    cursor.close()
    cnx.close()
    return listStudents

# Function to retrieve all the subjects for a class
def QueryClassSubject(idclass=""):
    cnx = mysql.connector.connect(**db.config)
    cursor = cnx.cursor()
    whereclause = ""
    if len(idclass) > 0:
        whereclause += "idclass = \"" + idclass + "\""
    if len(whereclause)>0:
      whereclause = "WHERE " + whereclause
    query_classsubject = ("SELECT idclass, idsubject, subjectname FROM vw_classsubject "+ whereclause)
    cursor.execute(query_classsubject)
    listClassSubject = []
    for classsubject in cursor:
      listClassSubject.append(classsubject)
    cursor.close()
    cnx.close()
    return listClassSubject

if __name__ == "__main__":
    getStudentsbyClass("12F2202223")