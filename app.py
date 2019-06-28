from flask import Flask, render_template, request, session, redirect, url_for
import hashlib
import sqlite3
from security.inputValidation import inputValidation, isAlphanumeric, isAlpha, isDigit, isBool
import login
import mainpageauditor
import mainpageAdministrador
import addAuditorUser
import updateUserr
import addAuditoriaa
from logRegister import logRegister
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'jerson'

userIn = ' '

@app.route('/')
def index():
    #recaptcha = RecaptchaField()
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def log():
    return login.login()


@app.route('/mainpage')
def mainpage():
    return mainpageauditor.mainpageauditor()

@app.route('/mainpageAdmin')
def mainpageAdmin():
    return mainpageAdministrador.mainpageAdministrador()

@app.route('/mainpageAdmin/updateUser')
def updateUser():
    if 'user' in session:
        if session['user'] == 1:
            return render_template('updateUser.html')
        else:
            return render_template('permition.html')
    else:
        return render_template('login.html')

@app.route('/updateUser', methods=['POST'])
def updtUser():
    return updateUserr.updateUserr()

@app.route('/mainpageAdmin/addAuditor')
def addAuditor():
    if 'user' in session:
        if session['user'] == 1:
            return render_template('addAuditor.html')
        else:
            return render_template('permition.html')
    else:
        return render_template('login.html')

@app.route('/addAuditor', methods=['POST'])
def addUser():
    return addAuditorUser.addAuditorUser()


@app.route('/mainpage/addAuditoria')
def addAuditoria():
    if 'user' in session:
        if session['user'] != 1:
            return render_template('addAuditoria.html')
        else:
            return render_template('permition.html')
    else:
        return render_template('login.html')

@app.route('/addAuditoria', methods=['POST'])
def addAudit():
    return addAuditoriaa.addAuditoriaa()

@app.route('/permition')
def permition():
    return render_template('permition.html')

@app.route('/index')
def logout():
    try:
        conn = sqlite3.connect('auditoria.db')
        cursor = conn.execute("SELECT USER from UTILIZADOR where ID = %s" % (session['user'],) )
        for row in cursor:
            user = row[0]
        session.pop('user', None)
        logRegister(user, 'logout', 'success', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
        return index()
    except:
        logRegister(user, 'logout', 'failure', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
        return "Logout failure" 


if __name__ == '__main__':
    app.run(debug = True)
