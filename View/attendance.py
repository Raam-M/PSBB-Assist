import mysql.connector
from datetime import date, datetime, timedelta
import dbconfig as db

#Function to add a new absentee into the attendance table
def AddAbsentee(idstudclass, dateabsent, absentreason=""):
    cnx = mysql.connector.connect(**db.config)
    cursor = cnx.cursor()
    add_absentee = ("INSERT INTO attendance "
               "(idstudclass, dateabsent, absentreason) "
               "VALUES (%s, %s, %s)")
    data_absentee = (idstudclass, dateabsent, absentreason)
    cursor.execute(add_absentee, data_absentee)
    cnx.commit()
    cursor.close()
    cnx.close()

#Function to delete an absentee from the attendance table
def DeleteAbsentee(idattendance):
    cnx = mysql.connector.connect(**db.config)
    cursor = cnx.cursor()
    delete_absentee = ("DELETE FROM attendance "
               "WHERE idattendance = %s")
    data_absentee = [idattendance]
    cursor.execute(delete_absentee, data_absentee)
    cnx.commit()
    cursor.close()
    cnx.close()

# Function to retrieve all the absentees for a class on a specified date
def QueryAbsentee(idclass, dateabsent):
    cnx = mysql.connector.connect(**db.config)
    cursor = cnx.cursor()
    whereclause = ""
    whereclause += "idclass = \"" + str(idclass) + "\" "
    whereclause += "AND dateabsent = \"" + dateabsent + "\""
  #  idstudent,studfname,studlname,gender,studdob,studadmissiondate,studexitdate,idstudclass,idclass,rollnumber,standard,
  #  division,acadyr,idattendance,dateabsent,absentreason
    query_absentee = ("SELECT idstudent,studfname,studlname,"
                        "idstudclass,idclass,rollnumber,standard,division,"
                        "idattendance,dateabsent,absentreason FROM vw_attendstudclass "
                        "WHERE " + whereclause)
    cursor.execute(query_absentee)
    dictabsentee = {}
    for absentee in cursor:
        dictabsentee[absentee[3]] = absentee
    cursor.close()
    cnx.close()
    return dictabsentee

if __name__ == "__main__":
    QueryAbsentee("12F2202223", "2022-11-13")