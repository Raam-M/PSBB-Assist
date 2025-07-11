import mysql.connector
from datetime import date, datetime, timedelta
import dbconfig as db

# Function to add a new session log in the sessionlog table
def AddSessionLog(idclass, idsubject, sessionnum, logcontent, logdate):
    cnx = mysql.connector.connect(**db.config)
    cursor = cnx.cursor()
    add_sessionlog = ("INSERT INTO sessionlog "
               "(idclass, idsubject, datelog, sessionnum, logcontent) "
               "VALUES (%s, %s, %s, %s, %s)")
    data_sessionlog = (idclass, idsubject, logdate, sessionnum, logcontent)
    cursor.execute(add_sessionlog, data_sessionlog)
    cnx.commit()
    cursor.close()
    cnx.close()

# Function to update an existing session log in the sessionlog table
def UpdateSessionLog(idsessionlog, logcontent):
    cnx = mysql.connector.connect(**db.config)
    cursor = cnx.cursor()
    today = datetime.now().date()  #+ timedelta(days=1)
    update_sessionlog = ("UPDATE sessionlog "
               "SET logcontent = %s"
               "WHERE idsessionlog = %s")
    data_sessionlog = (logcontent, idsessionlog)
    cursor.execute(update_sessionlog, data_sessionlog)
    cnx.commit()
    cursor.close()
    cnx.close()

# Function to retrieve all the session logs for a given class and date
def QuerySessLog(idclass, idsubject, sessionnum, datelog, logcontent):
    cnx = mysql.connector.connect(**db.config)
    cursor = cnx.cursor()
    today = datetime.now().date()  #+ timedelta(days=1)
    whereclause = ""
    if len(idclass) > 0:
        whereclause += "idclass = \"" + idclass + "\""
    if len(idsubject) > 0 :
        if(len(whereclause) > 0):
            whereclause += " AND idsubject = \"" + idsubject + "\""
        else:
            whereclause += "idsubject = \"" + idsubject + "\""
    if len(sessionnum) > 0 :
        if len(whereclause) > 0:
            whereclause += " AND sessionnum = \"" + sessionnum + "\""
        else:
            whereclause += "sessionnum = \"" + sessionnum + "\""
    if len(datelog) > 0 :
        if len(whereclause) > 0:
            whereclause += " AND datelog = \"" + datelog + "\""
        else:
            whereclause += "datelog = \"" + datelog + "\""
    if len(logcontent) > 0 :
        if len(whereclause) > 0:
            whereclause += " AND logcontent LIKE \"%" + logcontent + "%\""
        else:
            whereclause += "logcontent LIKE \"%" + logcontent + "%\""            
    query_sessionlog = ("SELECT idsessionlog, idclass, idsubject, subjectname, sessionnum, datelog, logcontent FROM vw_sesslogsubject "
               "WHERE " + whereclause)

    cursor.execute(query_sessionlog)
    listLogContent = []
    for logcontent in cursor:
        listLogContent.append(logcontent)
    cursor.close()
    cnx.close()
    return listLogContent


if __name__ == "__main__":
    QuerySessLog("","","","","G")