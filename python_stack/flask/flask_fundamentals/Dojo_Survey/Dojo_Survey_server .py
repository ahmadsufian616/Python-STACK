from logging import debug
from flask import Flask ,render_template,request
app=Flask((__name__),template_folder="template")


@app.route('/')
def form_get():
    return render_template("index.html")


@app.route('/result',methods=['POST'])
def test1():
    name=request.form["name"]
    loc=request.form["loc"]
    lan=request.form["lan"]
    com=request.form["com"]
    return render_template("result.html",name=name,loc=loc,com=com,lan=lan)




if __name__=='__main__':
    app.run(debug=True)



    