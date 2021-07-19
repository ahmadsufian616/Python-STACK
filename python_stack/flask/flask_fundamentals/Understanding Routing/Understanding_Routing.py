from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world1():
    return 'Hello World!'



@app.route('/dojo')
def hello_world2():
    return 'Dojo!'



@app.route('/say/<name>')
def hello_world3(name):
    return "Hi, "+name



@app.route('/repeat/<num>/<name>')
def hello_world4(num,name):
    return name*int(num)

if __name__ =="__main__":
    app.run(debug=True)  




