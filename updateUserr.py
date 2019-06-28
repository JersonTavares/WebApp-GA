from app import inputValidation, sqlite3, redirect, url_for, request, session
from datetime import datetime
from logRegister import logRegister

def updateUserr():
    try:
        conn = sqlite3.connect('auditoria.db')
        cursor = conn.execute("SELECT USER from UTILIZADOR where ID = %s" % (session['user'],) )
        for row in cursor:
            user = row[0]
        if inputValidation(request.form['name'], 'alphanumeric') and inputValidation(request.form['id'], 'digit'):
            cursor = conn.execute("SELECT USER from UTILIZADOR where USER = '%s'" % (request.form['name'],) )
            result = 0
            for row in cursor:
                result = result + 1
            if result == 0:
                conn = sqlite3.connect('auditoria.db')
                conn.execute("UPDATE UTILIZADOR set USER = '%s' where ID = %s" % (request.form['name'], request.form['id'] ))
                conn.commit()
                conn.close()
                logRegister(user, 'updateUser', 'success', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
                return redirect(url_for('mainpageAdmin'))
            else:
                logRegister(user, 'updateUser', 'failure', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
                return "User already exist"
        else:
            logRegister(user, 'updateUser', 'failure', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
            return "Input Error"
    except:
        logRegister(user, 'updateUser', 'failure', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
        return "Something went wrong"
