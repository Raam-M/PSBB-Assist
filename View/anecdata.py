import mysql.connector
from datetime import date, datetime, timedelta
import dbconfig as db

#AddAnecdote function will insert a new row in the anecdote table
#call this from anecdote module when a new anecdote is saved
def AddAnecdote(idstudclass, anecdate, idteacher, anectype, anecdesc):
    cnx = mysql.connector.connect(**db.config)
    cursor = cnx.cursor()
    add_anecdote = ("INSERT INTO anecdote "
               "(idstudclass, anecdate, idteacher, anectype, anecdesc) "
               "VALUES (%s, %s, %s, %s, %s)")
    data_anecdote = (idstudclass, anecdate, idteacher, anectype, anecdesc)
    cursor.execute(add_anecdote, data_anecdote)
    cnx.commit()
    cursor.close()
    cnx.close()

#call this method to save changes to an existing anecdote
#this function updates changes to the anecdote table using idanecdote
def UpdateAnecdote(idanecdote, anecdesc):
    cnx = mysql.connector.connect(**db.config)
    cursor = cnx.cursor()
    update_anecdote = ("UPDATE anecdote "
                       "SET anecdesc = %s"
                       "WHERE idanecdote = %s")
    data_anecdote = (anecdesc, idanecdote)
    cursor.execute(update_anecdote, data_anecdote)
    cnx.commit()
    cursor.close()
    cnx.close()

# This function will retrieve all the anecdotes for a specified class
# This uses the vw_anecdote view to do this
def QueryAnecdote(idclass):
    cnx = mysql.connector.connect(**db.config)
    cursor = cnx.cursor()
    whereclause = ""
    if len(idclass) > 0:
        whereclause += "idclass = \"" + idclass + "\""
    query_anecdote = ("SELECT idanecdote,idstudclass,anecdate,idteacher,anectype,anecdesc,"
                        "idstudent,studfname,studlname,gender,idclass,rollnumber,standard,division,acadyr,"
                        "teacherfname,teacherlname FROM vw_anecdote "
                        "WHERE " + whereclause)
    cursor.execute(query_anecdote)
    listanecdote = []
    for aneccontent in cursor:
        listanecdote.append(aneccontent)
    cursor.close()
    cnx.close()
    return listanecdote

if __name__ == "__main__":
    QueryAnecdote("12F2202223")