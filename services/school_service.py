from utility import db

def getSchools():
    query = db.db.cursor(dictionary=True)
    query.execute('SELECT * FROM admins')
    db.db.commit()
    result = query.fetchall()
    return result

def insertSchool(school_name, school_email, school_pwd, school_address, school_pin):
    query = db.db.cursor()
    sql = "INSERT INTO admins (school_name, school_email, school_pwd, school_address, school_pin) VALUES ('{}', '{}', '{}', '{}', '{}')".format(school_name, school_email, school_pwd, school_address, school_pin)
    query.execute(sql)
    result = query.lastrowid
    db.db.commit()
    return result


def isSchoolEmailExists(school_email):
    query = db.db.cursor()
    checkEmailSQL = "SELECT * FROM admins WHERE school_email = '{}'".format(school_email)
    query.execute(checkEmailSQL)

    schoolData = query.fetchall()

    print(schoolData)

    if(len(schoolData) > 0):
        return True

    return False







