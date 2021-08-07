from flask import flash,request,render_template,url_for
from flask.app import Flask
from werkzeug.utils import redirect

app=Flask(__name__)
@app.route('/')
def welcome():
    return render_template('index.html')
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>50:
        res='Pass'
    else:
        res='Fail'
    exp={'Score':score,'result':res}               
    return render_template('result.html',result=exp)     
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0

    science=str(request.form['Science'])
    maths=float(request.form['maths'])
    C=float(request.form['C'])
    python=float(request.form['Python'])
    total_score=(science+maths+C+python)/4
    return(redirect(url_for('success',score=total_score)))




if __name__=='__main__':
    app.run( )