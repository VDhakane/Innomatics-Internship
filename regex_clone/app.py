import re
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/search',methods=['POST'])
def search_function():
    string=request.form['in_1']
    txt=request.form['in_2']
    count = re.findall(txt ,string)
    
    return render_template('search.html',t=txt,s=string,m=len(count))
    

if __name__=='__main__':
    app.run(debug=True)
