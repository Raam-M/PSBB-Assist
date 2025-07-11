import mysql.connector
import dbconfig as db

# Function to retrieve class details from the classconfig table
def QueryClassConfig(idclass="", standard="", division="", acadyr=""):
    cnx = mysql.connector.connect(**db.config)
    cursor = cnx.cursor()
    whereclause = ""
    if len(idclass) > 0:
        whereclause += "idclass = \"" + idclass + "\""
    if len(standard) > 0 :
        if len(whereclause) > 0:
            whereclause += " AND standard = \"" + standard + "\""
        else:
            whereclause += "standard = \"" + standard + "\""
    if len(division) > 0 :
        if len(whereclause) > 0:
            whereclause += " AND division = \"" + division + "\""
        else:
            whereclause += "division = \"" + division + "\""
    if len(acadyr) > 0 :
        if len(whereclause) > 0:
            whereclause += " AND acadyr = \"" + acadyr + "\""
        else:
            whereclause += "acadyr = \"" + acadyr + "\""
    if len(whereclause)>0:
      whereclause = "WHERE " + whereclause
    query_classconfig = ("SELECT idclass, standard, division, acadyr FROM classconfig "+ whereclause)
    cursor.execute(query_classconfig)
    listClassConfig = []
    for classconfig in cursor:
      listClassConfig.append(classconfig)
    cursor.close()
    cnx.close()
    return listClassConfig

# Function to retrieve list of subjects applicable for a class
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
    QueryClassConfig()