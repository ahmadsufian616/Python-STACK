from logging import debug
from flask import Flask ,render_template,request
app=Flask((__name__),template_folder="template")

@app.route('/')
def test():
    print("hello")
    return render_template("index.html")


@app.route('/user',methods=['POST'])
def test1():
    name=request.form["name"]
    password=request.form["password"]
    return render_template("show.html",name_new=name,password_new=password)


if __name__=="__main__":
    app.run(debug=True)



