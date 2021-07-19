from flask import Flask, render_template
import math
app= Flask(__name__,template_folder ='template')
@app.route('/')
def check8():
    return render_template("index.html",num=4)
@app.route('/<num>')
def checknym(num):
    num=int(num)
    if(num%2==0):
        odd=False
        num=num/2
    else:
        odd=True
        num = math.floor(num/2)
    return render_template("index.html", num=int(num),odd=odd)
# @app.route('/<num1>/<num2>')
# def checkxy(num1,num2):
#     return render_template("index.html", num1=int(num1),num2=int(num2))


if __name__ =="__main__":
    app.run(debug=True) 
