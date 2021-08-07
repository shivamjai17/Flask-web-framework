from flask import Flask , render_template
import requests
import json
app =Flask(__name__)
@app.route('/')
def get_():
    return render_template('index.html')


if __name__=='__main__':
    app.run()    