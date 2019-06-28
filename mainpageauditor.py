from app import session, sqlite3, render_template
from datetime import datetime
from logRegister import logRegister

def mainpageauditor():
    try:
        conn = sqlite3.connect('auditoria.db')
        cursor = conn.execute("SELECT USER from UTILIZADOR where ID = %s" % (session['user'],) )
        for row in cursor:
            user = row[0]
        if 'user' in session:
            if session['user'] != 1:
                conn = sqlite3.connect('auditoria.db')
                conn.row_factory = sqlite3.Row
                cursor = conn.execute("SELECT * from AUDITORIA ")
                rows = cursor.fetchall()
                conn.close()
                logRegister(user, 'mainpageAuditor', 'success', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
                return render_template('mainpage.html', rows = rows)
            else:
                logRegister(user, 'mainpageAuditor', 'failure', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
                return render_template('permition.html')
        else:
            return render_template('login.html')
    except:
        logRegister(user, 'mainpageAuditor', 'failure', datetime.now().strftime("%m/%d/%Y,%H:%M:%S"))
        return "Something went wrong"
