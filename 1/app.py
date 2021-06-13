from flask import Flask,redirect,url_for
#wsgi application
app=Flask(__name__)
@app.route('/')
def wel():
    return 'Welcome to Flask and subcribe!'
@app.route('/one/<int:s>')
def come(s):
    return "Student is Pass "+str(s)


@app.route('/two/<int:s>')
def two(s):
    return "student is fail "+str(s)

@app.route('/results/<int:m>')
def result(m):
    re=""
    if m<50:
        re='two'
    else:
        re='one'
    return redirect(url_for(re,s=m))    


if __name__=='__main__':
    app.run(debug=True)