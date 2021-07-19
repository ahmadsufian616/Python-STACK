# from logging import debug
from flask import Flask,render_template,request,redirect,session
app=Flask(__name__,template_folder="template")
app.secret_key='a'
#app.count = 0
@app.route('/')
def counter():
    #if 'a' in session:
    session['count'] += 1
    return render_template('index.html',count=session['count'])
    

@app.route('/destroy_session ')
def counter1():

    session.clear()
    return render_template('index.html')
    


if __name__=='__main__':
    app.run(debug=True)