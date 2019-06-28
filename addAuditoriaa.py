from app import inputValidation, sqlite3, request, redirect, url_for, session
from datetime import datetime
from logRegister import logRegister

def addAuditoriaa():
    try:
        conn = sqlite3.connect('auditoria.db')
        cursor = conn.execute("SELECT USER from UTILIZADOR where ID = %s" % (session['user'],) )
        for row in cursor:
            user = row[0]
        if inputValidation(request.form['id'], 'digit') and inputValidation(request.form['name'], 'alphanumeric') \
            and inputValidation(request.form['description'], 'alphanumeric') :
            conn = sqlite3.connect('auditoria.db')
            conn.execute("INSERT INTO AUDITORIA (ID, NAME, STDATE, ENDATE, DESCRIPTION, AUDITOR) VALUES (?,?,?,?,?,?) ", \
                        (request.form['id'], request.form['name'], request.form['stdate'], request.form['endate'], \
                         request.form['description'], user))
            conn.commit()
            conn.close()
            logRegister(user, 'addAuditoria', 'success', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
            return redirect(url_for('mainpage'))
        else:
            logRegister(user, 'addAuditoria', 'failure', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
            return "Input Error"
    except:
        logRegister(user, 'addAuditoria', 'failure', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
        return "Something went wrong"
