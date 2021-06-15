from flask import Flask,url_for,render_template,request
from werkzeug.utils import html, redirect
app=Flask(__name__)
@app.route('/')
def welcome():
    return render_template('index.html')
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:   
        res="FAIL"
    return render_template('result.html',result=res,sco=score)        

@app.route('/submit',methods=['GET','POST'])
def submit():
    total_score=0
    science=float(request.form['Science'])
    maths=float(request.form['maths'])
    C=float(request.form['C'])
    python=float(request.form['Python'])
    total_score=(science+maths+C+python)/4
    return redirect(url_for('success',score=total_score))    



if __name__ =='__main__':
    app.run(debug=True)
