from flask import Flask, render_template, request, url_for, jsonify

## create a simple flask application
app=Flask(__name__)
@app.route("/",methods=["GET"])

def welcome():
    return "Welcome to welcome page"
@app.route("/index",methods=["GET"])

def index():
    return "Welcome to index page"

@app.route('/form',methods=["GET","POST"])
def form():
    if request.method == "GET":
        return render_template('form.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
        avg_mark = (maths+science+history)/3
        return render_template('form.html', score=avg_mark)

@app.route('/calculate',methods=["POST"])
def calculate():
    data=request.get_json()
    print(data['a'])
    a_val= data['a']
    b_val= data['b']
    return jsonify(a_val+b_val)

if __name__:
    app.run(debug=True)

