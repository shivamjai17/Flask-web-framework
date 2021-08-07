from flask import Flask , render_template,redirect,url_for,send_file
import requests
import json
import pandas as pd
app =Flask(__name__,static_url_path='/stati     c')
@app.route('/')
def get_():
    name=['shivam','rashmi','shiv']
    age=[20,22,17]
    a={
        'name':name,
        'age':age
    }
    df=pd.DataFrame(a)


    return render_template('index.html',tables=[df.to_html(classes='d')])
    # return df.to_html(header=True,table_id="table") 
 

if __name__=='__main__':
    app.run(debug=True)    