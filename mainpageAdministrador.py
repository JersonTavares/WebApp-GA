from app import session, render_template, sqlite3
from datetime import datetime
from logRegister import logRegister

def mainpageAdministrador():
    try:
        conn = sqlite3.connect('auditoria.db')
        cursor = conn.execute("SELECT USER from UTILIZADOR where ID = %s" % (session['user'],) )
        for row in cursor:
            user = row[0]
        if 'user' in session:
            if session['user'] == 1:
                conn = sqlite3.connect('auditoria.db')
                conn.row_factory = sqlite3.Row
                cursor = conn.execute("SELECT * from UTILIZADOR ")
                rows = cursor.fetchall()
                conn.close()
                logRegister(user, 'mainpageAdministrador', 'success', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
                return render_template('mainpageAdmin.html', rows = rows)
            else:
                logRegister(user, 'mainpageAdministrador', 'failure', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
                return render_template('permition.html')
        else:
            return render_template('login.html')
    except:
        logRegister(user, 'mainpageAdministrador', 'failure', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
        return "Something went wrong"
