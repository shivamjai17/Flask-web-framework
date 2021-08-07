from flask import Flask , render_template ,redirect
import json


app=Flask(__name__)

@app.route('/')
def hellow():
    details=[5,2,4,6,3,4]
    return render_template('index.html')
@app.route("/home")
def home():
    d=[4,5,3,6,2,3]
    return render_template("home.html",a=d)
if __name__=='__main__':
    app.run(debug=True)