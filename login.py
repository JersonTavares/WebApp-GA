from app import inputValidation, request, redirect, url_for, session, hashlib, sqlite3, index, datetime, logRegister

# userIn = '_'
def login():
    try:
        # global userIn
        # userIn = request.form['user']
        # logRegister(request.form['user'], 'login', 'trying', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
        if inputValidation(request.form['user'], 'alphanumeric') and inputValidation(request.form['password'], 'alphanumeric'):
            salt = 'esmael'
            p = (request.form['password']+salt).encode()
            conn = sqlite3.connect('auditoria.db')
            #password = generate_password_hash(request.form['password'])
            cursor = conn.execute("SELECT * from UTILIZADOR where \
                    USER = '%s' and PASSWORD = '%s'" % (request.form['user'], hashlib.sha512(p).hexdigest()) )
            result = 0
            for row in cursor:
                userID = row[0]
                userTYPE = row[3]
                result = result + 1
            if result == 1:
                session['user'] = userID
                logRegister(request.form['user'], 'login', 'success', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
                if userTYPE == 'admin':
                    conn.close()
                    return redirect(url_for('mainpageAdmin'))
                else:
                    conn.close()
                    return redirect(url_for('mainpage'))
            else:
                conn.close()
                logRegister(request.form['user'], 'login', 'failure', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
                return index()
        else:
            logRegister(request.form['user'], 'login', 'failure', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
            return "Input Error"
    except:
        return "Something went wrong"
