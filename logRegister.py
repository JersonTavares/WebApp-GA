# from flask import Flask, session
# import sqlite3

# app = Flask(__name__)


# @app.route('/')
def logRegister(user, action, status, time):
    try:
        f = open('logFile.txt', 'a')
        f.write(user +" "+ action +" "+ status +" "+ time)
        f.write('\n')
        f.close()
    except:
        return "Something went wrong"

# def userIn():
#         userID = session['user']
    # try:
        # conn = sqlite3.connect('auditoria.db')
        # cursor = conn.execute("SELECT * from UTILIZADOR where ID = %s" ,UserID)
        # conn.close()
        # return cursor

        # result = 0
        # for row in cursor:
        #     user = row[1]
        #     result = result + 1
        # return user
    # except:
    #     return "testing"
# if __name__ == '__main__':
#     app.run(debug = True)
