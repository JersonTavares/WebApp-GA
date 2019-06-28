from app import inputValidation, request, redirect, url_for, hashlib, sqlite3, session
from datetime import datetime
from logRegister import logRegister
import login

def addAuditorUser():
    # return login.userIn

    try:
        conn = sqlite3.connect('auditoria.db')
        cursor = conn.execute("SELECT USER from UTILIZADOR where ID = %s" % (session['user'],) )
        for row in cursor:
            user = row[0]
        if inputValidation(request.form['id'], 'digit') and inputValidation(request.form['name'], 'alpha') \
                and inputValidation(request.form['age'], 'digit')\
                and inputValidation(request.form['address'], 'alphanumeric') and inputValidation(request.form['user'], 'alphanumeric') \
                and inputValidation(request.form['password'], 'alphanumeric') and inputValidation(request.form['cpassword'], 'alphanumeric')\
                and request.form['password'] == request.form['cpassword']:


                cursor = conn.execute("SELECT USER from UTILIZADOR where USER = '%s'" % (request.form['user'],) )
                result = 0
                for row in cursor:
                    result = result + 1
                if result == 0:
                    salt = 'esmael'
                    p = (request.form['password']+salt).encode()
                    #hashed_password = hashlib.sha512(password + salt).hexdigest()
                    conn = sqlite3.connect('auditoria.db')
                    conn.execute("INSERT INTO AUDITOR (ID, NAME, EMAIL, AGE, ADDRESS) VALUES (?,?,?,?,?) ", \
                                (request.form['id'], request.form['name'], request.form['email'], request.form['age'], request.form['address']))
                    conn.execute("INSERT INTO UTILIZADOR (ID, USER, PASSWORD, TYPE) VALUES (?,?,?,?) ", \
                                (request.form['id'], request.form['user'], hashlib.sha512(p).hexdigest(), request.form['type']))
                    conn.commit()
                    conn.close()
                    logRegister(user, 'addAuditor', 'success', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
                    return redirect(url_for('mainpageAdmin'))
                else:
                    logRegister(user, 'addAuditor', 'failure', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
                    return "User already exist"
        else:
            logRegister(user, 'addAuditor', 'failure', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
            return "Input Error"
    except:
        logRegister(user, 'addAuditor', 'failure', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
        return "Something went wrong"
