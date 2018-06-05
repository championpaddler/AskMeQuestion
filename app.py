import json
import request
import random
import sqlite3
conn = sqlite3.connect('f.db')
c = conn.cursor()
c.execute("SELECT  * FROM question")
t=c.fetchall()
GREETINGS=[["hello"],["bye"],["Who are you"]]
d=[]
for i in t:
    d=[i[0]]
    GREETINGS.append(d)
    d=[]

GREETING_RESPONSES=[["sup bro", "hey", "hey you get my snap?"],["Ok Bye"],["I am your assistant NSS Conselling Bot"]]
d=[]
for i in t:
    d=[i[1]]
    GREETING_RESPONSES.append(d)
    d=[]
    
def check_for_greeting(sen):
    
    for i in range(0,len(GREETINGS)):
        for j in  GREETINGS[i]:
            if(sen==j):
                return (random.choice(GREETING_RESPONSES[i]))
    else:
        return ("Try Again")
    
from flask import Flask,render_template, request
app = Flask(__name__)


result=[]
res=[]
@app.route('/',methods = ['POST', 'GET'])
def index():
    return render_template("a.html",result=[],test=GREETINGS)

@app.route('/signUpUser',methods = ['POST'])
def signUpUser():
    user =  request.form['username'];
    
    result=check_for_greeting(user)
    
    return json.dumps([{"q":user},{"a":result}])

    
if __name__ == '__main__':
    app.run()
