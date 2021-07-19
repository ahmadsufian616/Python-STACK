from flask import Flask,render_template
app = Flask(__name__,template_folder='template')
@app.route('/play')
def Playground1 ():
    return render_template("index.html", num=3,color='blue')

@app.route('/play/<x>')
def Playground2 (x ):
    return render_template("index.html", num=int(x), color='blue')

@app.route('/play/<x>/<color>')
def Playground3 (x , color):
    return render_template("index.html", num=int(x),color=color)

if __name__=="__main__":
    app.run(debug=True)